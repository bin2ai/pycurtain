# create an enum of the different img2img methods
from enum import Enum
from PIL import Image
from pycurtain.img2img.stability_ai import StabilityAI


class Img2ImgMethod(Enum):
    # stability_ai
    STABILITY_AI = 0
    # TODO: add more methods


class Img2Img:
    def __init__(self, method: Img2ImgMethod):
        # raise exception if method is not supported
        if method not in Img2ImgMethod:
            raise Exception("Method not supported")

        self.method = method

    def run(self, img_i: Image.Image, prompt: str = None, img_m: Image.Image = None, seed: int = None) -> Image.Image:

        # stability_ai
        if self.method == Img2ImgMethod.STABILITY_AI:
            self.img_o = StabilityAI().run(img_i, prompt, img_m, seed)

        # return result
        return self.img_o
