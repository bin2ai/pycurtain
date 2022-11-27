from PIL import Image


class Upscaler():
    img_i: Image.Image
    img_o: Image.Image
    api_key: str
    scale: int
