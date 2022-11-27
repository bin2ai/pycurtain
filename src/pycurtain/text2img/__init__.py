# create an enum of the different text2img methods
from enum import Enum
from PIL import Image
from pycurtain.text2img.stability_ai import StabilityAI


class Text2ImgMethod(Enum):
    # stability_ai
    STABILITY_AI = 0
    # TODO: add more models here


class Text2Img:
    def __init__(self, method: Text2ImgMethod):
        # raise exception if method is not supported
        if method not in Text2ImgMethod:
            raise Exception("Method not supported")

        self.method = method

    def run(self, prompt: str = None, seed: int = None) -> Image.Image:

        # stability_ai
        if self.method == Text2ImgMethod.STABILITY_AI:
            self.img_o = StabilityAI().run(prompt, seed)

        # return result
        return self.img_o
