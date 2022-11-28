from PIL import Image
# local imports
from pycurtain.source import SourceType as SourceType
from pycurtain.source import Source_AI as Source_AI


# call edit task based on the input source
def edit(source: Source_AI, prompt: str, img_i: Image.Image, img_m: Image.Image) -> Image.Image:
    if source.source_type == SourceType.STABLE_DIFFUSION:
        return source.source.edit(prompt=prompt, img_i=img_i, img_m=img_m)
    elif source.source_type == SourceType.DALLE2:
        return source.source.edit(prompt=prompt, img_i=img_i, img_m=img_m)
    else:
        raise Exception("Invalid source type")


# call generate task based on the input source
def generate(source: Source_AI, prompt: str) -> Image.Image:
    if source.source_type == SourceType.STABLE_DIFFUSION:
        return source.source.generate(prompt=prompt)
    elif source.source_type == SourceType.DALLE2:
        return source.source.generate(prompt=prompt)
    else:
        raise Exception("Invalid source type")


# call vary task based on the input source
def vary(source: Source_AI, prompt: str, img_i: Image.Image) -> Image.Image:
    if source.source_type == SourceType.STABLE_DIFFUSION:
        return source.source.vary(prompt=prompt, img_i=img_i)
    elif source.source_type == SourceType.DALLE2:
        return source.source.vary(img_i=img_i)
    else:
        raise Exception("Invalid source type")


# call upscale task based on the input source
def upscale(source: Source_AI, img_i: Image.Image) -> Image.Image:
    if source.source_type == SourceType.DEEP_AI:
        return source.source.upscale(img_i=img_i)
    else:
        raise Exception("Invalid source type")
