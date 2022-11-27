# create an enum of the different upscaling methods
from enum import Enum
from PIL import Image
from pycurtain.upscaler.deep_ai import DeepAI


class UpscalerMethod(Enum):
    # deep_ai.com
    DEEP_AI = 0
    # TODO: add more methods here


class Upscaler:
    # variable init_img Image.Image
    img_i: Image.Image
    img_o: Image.Image
    method: UpscalerMethod

    def __init__(self, method: UpscalerMethod):
        # raise exception if method is not supported
        if method not in UpscalerMethod:
            raise Exception("Method not supported")

        self.method = method

    def run(self, img: Image.Image, scale: int = 2) -> Image.Image:

        # upscale the image
        if self.method == UpscalerMethod.DEEP_AI:
            img_o = DeepAI().run(img)

        # return result
        return img_o
