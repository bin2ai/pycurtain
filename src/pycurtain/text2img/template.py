from PIL import Image


class Text2Img:
    img_i: Image.Image
    img_o: Image.Image
    img_m: Image.Image
    prompt: str
    seed: int
    api_key: str
