import base64
from io import BytesIO
from PIL import Image, ImageDraw
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


# zoom in image by a factor, shrink pixels of image centered, and crop the rest
def crop_out_by_factor(img: Image.Image, factor: int) -> Image.Image:
    width, height = img.size
    img = img.resize((width * factor, height * factor))
    img = img.crop((width * (factor - 1) / 2, height * (factor - 1) / 2,
                    width * (factor + 1) / 2, height * (factor + 1) / 2))
    return img


def crop_out_by_pixel(img: Image.Image, pixel: int) -> Image.Image:
    width, height = img.size
    img = img.resize((width + pixel, height + pixel))
    img = img.crop((pixel, pixel, width, height))
    return img


# zoom out image by a factor, shrink pixels of image centered, and fill the rest with transparent pixels
def crop_in_by_factor(img: Image.Image, factor: int) -> Image.Image:
    width, height = img.size
    # create canvas with transparent pixels
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    img = img.resize(size=(width//factor, height//factor))
    # paste image to canvas in the center, keep the original image size
    canvas.paste(img, box=(width//2 - width // (2 * factor),
                 height // 2 - height // (2 * factor)))

    return canvas


def crop_in_by_pixel(img: Image.Image, pixel: int) -> Image.Image:
    width, height = img.size
    # create canvas with transparent pixels
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    img = img.resize(size=(width-pixel, height-pixel))
    # paste image to canvas in the center, keep the original image size
    canvas.paste(img, box=(pixel//2, pixel//2))
    return canvas


# create black and white mask where init image transparent pixels are converte to black and opaque pixels are converted to white
def create_mask_from_transparent(img: Image.Image) -> Image.Image:
    img_o = img.convert('RGBA')
    data = img_o.getdata()
    new_data = []
    for item in data:
        if item[3] == 255:
            new_data.append((255, 255, 255, 255))
        else:
            new_data.append((0, 0, 0, 255))
    img_o.putdata(new_data)
    return img_o


# zoom in on image by pixel amount, return image of same size
def zoom_at(img: Image.Image, pixel) -> Image.Image:
    w, h = img.size
    # crop to center
    img = img.crop((pixel, pixel, w-pixel, h-pixel))
    # resize to original size
    img = img.resize((w, h))
    return img


# overlay two images
def overlay(img1: Image.Image, img2: Image.Image) -> Image.Image:
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA")
    img = Image.alpha_composite(img1, img2)
    return img


# create a circle mask
def create_circle_mask(size: tuple) -> Image.Image:
    img_o = Image.new('L', size, 0)
    draw = ImageDraw.Draw(img_o)
    draw.ellipse((0, 0) + size, fill=255)
    return img_o


# turn black pixels into white, and white pixels into black
def invert(img: Image.Image) -> Image.Image:
    img_o = img.convert('RGBA')
    data = img_o.getdata()
    new_data = []
    for item in data:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((255, 255, 255, 255))
        else:
            new_data.append((0, 0, 0, 255))
    img_o.putdata(new_data)
    return img_o


if __name__ == "__main__":
    # test zoom and zoom_out
    img = Image.open("tests\\test.png")
    # print size
    print(img.size)
    img2 = crop_out_by_factor(img, 2)
    # print size
    print(img.size)
    img2.save("tests\\test_001_zoom.png")
    img = crop_in_by_factor(img, 2)
    # print size
    print(img.size)
    img.save("tests\\test_001_zoom_out.png")
