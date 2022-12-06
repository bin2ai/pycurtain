import enum
import os
from typing import List, Tuple
from PIL import Image
import replicate
# local imports
from pycurtain.utility.image import download_img, pil_to_base64
import pycurtain.secrete.stuff as shh
from pycurtain.source.protos.image import TaskImage

# list all valid pixel scalars as enum


class Pixels(enum.Enum):
    pixels_128: int = 128
    pixels_256: int = 256
    pixels_384: int = 384
    pixels_448: int = 448
    pixels_512: int = 512
    pixels_576: int = 576
    pixels_640: int = 640
    pixels_704: int = 704
    pixels_768: int = 768
    pixels_832: int = 832
    pixels_896: int = 896
    pixels_960: int = 960
    pixels_1024: int = 1024


class ReplicateStableDiffusion(TaskImage):

    # find versions here
    # https://replicate.ai/stability-ai/stable-diffusion/versions
    version = None

    def __init__(self, api_key: str = None):
        self.api_key = api_key
        # get os environment variable deep_ai, raise exception if not found
        if api_key is None:
            self.api_key = os.environ.get(shh.REPLICATE_API_TOKEN)
            if self.api_key is None:
                raise Exception(
                    "Replicate API Key not found. Please set the environment variable REPLICATE_API_TOKEN")

        self.model = replicate.models.get("stability-ai/stable-diffusion")
        self.version = self.model.versions.get(
            "27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")

    # function that validates width and hieghtheight" and is not larger than 1024x768 or 768x1024

    def __validate_size(self, width: Pixels, height: Pixels) -> Tuple[Pixels, Pixels]:
        if width.value == 1024 and height.value > 768 or height.value == 1024 and width.value > 768:
            raise ValueError("width or height cannot be larger than 1024")
        else:
            return width, height

    # generate image from prompt

    def generate(self, prompt: str, width: Pixels = Pixels.pixels_512, height: Pixels = Pixels.pixels_512, seed: int = None) -> List[Image.Image]:
        width, height = self.__validate_size(width, height)
        url = self.version.predict(
            prompt=prompt,
            seed=seed,
            width=width.value,
            heigh=height.value
        )[0]
        img = download_img(url)
        return [img]

    # edit image from prompt

    def edit(self, prompt: str, img_m: Image.Image, img_i: Image.Image, width: Pixels = Pixels.pixels_512, height: Pixels = Pixels.pixels_512, seed: int = None) -> List[Image.Image]:
        width, height = self.__validate_size(width, height)
        img_i = pil_to_base64(img_i)
        img_m = pil_to_base64(img_m)
        url = self.version.predict(
            width=width.value,
            height=height.value,
            prompt=prompt,
            seed=seed,
            init_image="data:image/png;base64,{}".format(img_i),
            mask="data:image/png;base64,{}".format(img_m),
        )[0]
        img = download_img(url)
        return [img]

    def vary(self, img_i: Image.Image, width: Pixels = Pixels.pixels_512, height: Pixels = Pixels.pixels_512, seed: int = None, prompt: str = None) -> List[Image.Image]:
        width, height = self.__validate_size(width, height)
        img_i = pil_to_base64(img_i)
        url = self.version.predict(
            width=width.value,
            height=height.value,
            seed=seed,
            init_image="data:image/png;base64,{}".format(img_i),
        )[0]
        img = download_img(url)
        return [img]
