import os
from typing import List
from PIL import Image
import requests
# local imports
import pycurtain.secrete.stuff as shh
from pycurtain.utility.image import pil_img_to_byte_array, download_img
from pycurtain.source.protos.image import TaskImage


class DeepAI(TaskImage):

    def __init__(self, api_key: str = None):

        # get os environment variable deep_ai, raise exception if not found
        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.environ.get(shh.DEEP_AI_API_KEY)
            if self.api_key is None:
                raise Exception(
                    "DEEP AI API KEY environment variable not found")

    # takes image and returns upsampled image
    def upscale(self, img_i: Image.Image) -> List[Image.Image]:

        if img_i is None:
            raise Exception("img_i is None")

        # get the image as a byte array
        img_i_bytes = pil_img_to_byte_array(img_i)

        # create the request
        data = requests.post(
            "https://api.deepai.org/api/torch-srgan",
            files={
                'image': img_i_bytes
            },
            headers={'api-key': self.api_key}
        ).json()

        # for key in data:
        #     print(key)
        #     print(data[key])

        if 'output_url' in data:
            url = data['output_url']
        else:
            return None

        # download the image from the response
        img_o = download_img(url)

        # wrap image in list
        return [img_o]
