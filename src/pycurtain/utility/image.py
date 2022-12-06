import base64
from io import BytesIO
from PIL import Image
import requests


# download image from url
def download_img(url: str) -> Image.Image:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


# convert PIL image to byte array
def pil_img_to_byte_array(img: Image.Image) -> bytes:
    img = img.convert("RGBA")
    img_bytes = BytesIO()
    if img.format is None:
        img.format = "PNG"

    img.save(img_bytes, format=img.format)
    if img is None:
        raise Exception("Image is Invalid")
    return img_bytes.getvalue()


# turn pixels of certain value into transparent pixels
def pixel_transparency(img: Image.Image, pixel_value: tuple) -> Image.Image:
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((pixel_value[0], pixel_value[1], pixel_value[2], 0))
        else:
            newData.append(item)
    img.putdata(newData)
    return img


# convert base64 to Pil.Image
def base64_to_pil(img_base64: str):
    img_bytes = base64.b64decode(img_base64)
    img = Image.open(BytesIO(img_bytes))
    return img


# encode image to base64
def pil_to_base64(img: Image.Image) -> str:
    img_bytes = pil_img_to_byte_array(img)
    img_base64 = base64.b64encode(img_bytes)
    return img_base64.decode("utf-8")
