from typing import List
from PIL import Image as PIL_Image
# local imports
from pycurtain.source import SourceImage, SourceImageType, SourceText


# prototype
class Image():

    def __init__(self, source: SourceImageType):
        self.source: SourceImage = SourceImage(source)

    # call edit task based on the input source

    def edit(self, prompt: str, img_i: PIL_Image.Image, img_m: PIL_Image.Image) -> List[PIL_Image.Image]:

        return self.source.source.edit(prompt=prompt, img_i=img_i, img_m=img_m)

    # call generate task based on the input source

    def generate(self, prompt: str) -> List[PIL_Image.Image]:
        # if source.source_type in SourceType
        return self.source.source.generate(prompt=prompt)

    # call vary task based on the input source

    def vary(self, prompt: str, img_i: PIL_Image.Image) -> List[PIL_Image.Image]:
        return self.source.source.vary(prompt=prompt, img_i=img_i)

    # call upscale task based on the input source

    def upscale(self, img_i: PIL_Image.Image) -> List[PIL_Image.Image]:
        return self.source.upscale(img_i=img_i)


class Text():

    def __init__(self, source: SourceText):
        self.source = source

    def summarize(source: SourceText, prompt: str) -> str:
        return source.source.summarize(prompt=prompt)

    def fix_grammar(source: SourceText, prompt: str) -> str:
        return source.source.fix_grammar(prompt=prompt)

    def tag(source: SourceText, prompt: str) -> str:
        return source.source.tag(prompt=prompt)


# list all public methods in image tasks
def list_image_tasks():
    return [e for e in Image.__dict__ if not e.startswith("__")]


# list all public methods in text tasks
def list_text_tasks():
    return [e for e in Text.__dict__ if not e.startswith("__")]


# test image task
if __name__ == "__main__":

    # test image task
    img_task = Image(SourceImageType.REPLICATE)
    img = img_task.generate(prompt="airplane flying over a bowl of chili")[0]
    img.save("test.png")
