import os
from PIL import Image
import requests
from io import BytesIO

# local imports
from pycurtain.upscaler.template import Upscaler
import pycurtain.secrete.stuff as shh


class DeepAI(Upscaler):

    def __init__(self, api_key: str = None):

        self.api_key = api_key

        # get os environment variable deep_ai, raise exception if not found
        if self.api_key is None:
            self.api_key = os.environ.get(shh.DEEP_AI_API_KEY)
            if self.api_key is None:
                raise Exception(
                    "DEEP AI API KEY environment variable not found")

    def run(self, img_i: Image.Image, scale: int = 1) -> Image.Image:

        if img_i is None:
            raise Exception("img_i is None")

        # get the image as a byte array
        img_byte_arr = BytesIO()
        img_i.save(img_byte_arr, format=img_i.format)
        img_byte_arr = img_byte_arr.getvalue()

        # create the request
        data = requests.post(
            "https://api.deepai.org/api/torch-srgan",
            files={
                'image': img_byte_arr
            },
            headers={'api-key': self.api_key}
        ).json()

        for key in data:
            print(key)
            print(data[key])

        if 'output_url' in data:
            url = data['output_url']
        else:
            return None

        # download the image from the response
        response = requests.get(url)
        img_o = Image.open(BytesIO(response.content))

        # return the image
        return img_o
