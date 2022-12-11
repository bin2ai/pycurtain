import enum
import os
from typing import List, Tuple
from PIL import Image
import replicate
# local imports
from pycurtain.utility.image import download_img, pil_to_base64
import pycurtain.secrete.stuff as shh
from pycurtain.source.protos.image import TaskImage


class ReplicateModel():
    model_name = None
    version = None

    def __init__(self, model_name: str, version: str):
        self.model_name = model_name
        self.version = version


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


replicate_stable_diffusion = ReplicateModel(
    model_name="stability-ai/stable-diffusion", version="27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
replicate_mid_journey = ReplicateModel(
    model_name="prompthero/openjourney", version="9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")
replicate_interrogate = ReplicateModel(
    model_name="methexis-inc/img2prompt", version="50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5")


class ReplicateStableDiffusion(TaskImage):

    # find versions here
    # https://replicate.ai/stability-ai/stable-diffusion/versions
    version = None
    model_name = None

    def __set_model(self, model: ReplicateModel):
        # if current model is not the same as the model_name, set model to model_name
        if self.model_name == model.model_name and self.version == model.version:
            return
        if self.model_name != model.model_name:
            self.model_name = model.model_name
            self.model = replicate.models.get(self.model_name)
        if self.version != model.version:
            self.version = model.version
            self.version = self.model.versions.get(self.version)

    def __init__(self, api_key: str = None):
        self.api_key = api_key
        # get os environment variable deep_ai, raise exception if not found
        if api_key is None:
            self.api_key = os.environ.get(shh.REPLICATE_API_TOKEN)
            if self.api_key is None:
                raise Exception(
                    "Replicate API Key not found. Please set the environment variable REPLICATE_API_TOKEN")

    # function that validates width and hieghtheight" and is not larger than 1024x768 or 768x1024

    def __validate_size(self, width: Pixels, height: Pixels) -> Tuple[Pixels, Pixels]:
        if width.value == 1024 and height.value > 768 or height.value == 1024 and width.value > 768:
            raise ValueError("width or height cannot be larger than 1024")
        else:
            return width, height

    # generate image from prompt

    def generate(self, prompt: str, width: Pixels = Pixels.pixels_512, height: Pixels = Pixels.pixels_512, seed: int = None) -> List[Image.Image]:
        self.__set_model(replicate_stable_diffusion)
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
        self.__set_model(replicate_stable_diffusion)
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
        self.__set_model(replicate_stable_diffusion)
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

    def interrogate(self, img: Image.Image) -> str:
        self.__set_model(replicate_interrogate)
        output = self.version.predict(
            image='data:image/png;base64,{}'.format(pil_to_base64(img)))
        return output
