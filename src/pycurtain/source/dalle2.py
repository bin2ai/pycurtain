from enum import Enum
import os
from typing import List
from PIL import Image
import openai
# local imports
import pycurtain.secrete.stuff as shh
from pycurtain.utility.image import download_img, pil_img_to_byte_array, pixel_transparency
from pycurtain.source.protos.image import TaskImage


# image size types
class SizeType(Enum):
    SMALL = 1  # 256x256
    MEDIUM = 2  # 512x512
    LARGE = 3  # 1024x1024


# DALLE2 model access from OpenAI
class DALLE2(TaskImage):
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        # get os environment variable deep_ai, raise exception if not found
        if api_key is None:
            self.api_key = os.environ.get(shh.OPENAI_API_KEY)
            # print(api_key)
            if self.api_key is None:
                raise Exception(
                    "Open AI Dalle2 API KEY environment variable not found")
            openai.api_key = self.api_key

    # takes prompt and returns output image
    def generate(self, prompt: str, size: SizeType = SizeType.MEDIUM) -> List[Image.Image]:

        if prompt is None:
            raise Exception("Prompt is required")

        # create a request
        res = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size_type_to_string(size)
        )

        # get url of image
        img_url = res["data"][0]["url"]
        # download img
        img_o = download_img(img_url)
        # wrap image in list
        return [img_o]

    # takes prompt image and mask and returns output image
    def edit(self, prompt: str, img_i: Image.Image, img_m: Image.Image, size: SizeType = SizeType.MEDIUM) -> List[Image.Image]:

        if prompt is None:
            raise Exception("Prompt is required")
        if img_i is None:
            raise Exception("Image input is None")
        if img_m is None:
            raise Exception("Image mask is None")

        # convert black pixels in mask to transparent using pixel_transparency
        img_m = pixel_transparency(img_m, (0, 0, 0))

        # img_m.show()
        # exit()
        # convert images to byte arrays
        img_i_bytes = pil_img_to_byte_array(img_i)
        img_m_bytes = pil_img_to_byte_array(img_m)

        # create a request
        res = openai.Image.create_edit(
            image=img_i_bytes,
            mask=img_m_bytes,
            prompt=prompt,
            n=1,
            size=size_type_to_string(size)
        )
        # get url of image
        img_url = res["data"][0]["url"]
        # download_img
        img_o = download_img(img_url)

        # wrap image in list
        return [img_o]

    # takes prompt image and returns a variation of the image
    def vary(self, img_i: Image.Image, size: SizeType = SizeType.MEDIUM) -> List[Image.Image]:

        if img_i is None:
            raise Exception("Image input is None")

        # convert images to byte arrays
        img_i_bytes = pil_img_to_byte_array(img_i)

        # create a request
        res = openai.Image.create_variation(
            image=img_i_bytes,
            n=1,
            size=size_type_to_string(size)
        )
        # get url of image
        img_url = res["data"][0]["url"]
        # download_img
        img_o = download_img(img_url)
        # wrap image in list
        return [img_o]


# convert size type to string
def size_type_to_string(size_type: SizeType) -> str:
    if size_type == SizeType.SMALL:
        return "256x256"
    elif size_type == SizeType.MEDIUM:
        return "512x512"
    elif size_type == SizeType.LARGE:
        return "1024x1024"
    else:
        raise Exception("Invalid size type")
