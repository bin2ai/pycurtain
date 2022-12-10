from typing import List
from PIL import Image

# prototype


class TaskImage():

    api_key: str = None

    def __init__(self, api_key: str = None):
        # raise exception if this function is not overriden
        raise Exception(
            "__init__() function not implemented for this SourceImageType")

    def generate(self, prompt: str, width: int, height: int, seed: int = None) -> List[Image.Image]:
        # raise exception if this function is not overriden
        raise Exception(
            "generate() function not implemented for this SourceImageType")

    def edit(self, prompt: str, img_i: Image.Image, img_m: Image.Image, width: int, height: int, seed: int = None) -> List[Image.Image]:
        # raise exception if this function is not overriden
        raise Exception(
            "edit() function not implemented for this SourceImageType")

    def vary(self, prompt: str, img_i: Image.Image, img_m: Image.Image, width: int, height: int, seed: int = None) -> List[Image.Image]:
        # raise exception if this function is not overriden
        raise Exception(
            "vary() function not implemented for this SourceImageType")

    def upscale(self, img_i: Image.Image) -> List[Image.Image]:
        # raise exception if this function is not overriden
        raise Exception(
            "upscale() function not implemented for this SourceImageType")

    def interrogate(self, img: Image.Image) -> str:
        # raise exception if this function is not overriden
        raise Exception(
            "interrogate() function not implemented for this SourceImageType")
