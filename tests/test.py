from PIL import Image
import os
# local imports
from pycurtain import Upscaler, UpscalerMethod
from pycurtain import Img2Img, Img2ImgMethod
from pycurtain import Text2Img, Text2ImgMethod

# location of this file
file_path = os.path.dirname(os.path.realpath(__file__))


# test upscaler
def test_upscaler(method: UpscalerMethod) -> bool:
    try:
        try:
            img_i = Image.open("{}\\test.png".format(file_path))
        except FileNotFoundError:
            return False

        # upscale the image
        img_o = Upscaler(method).run(img_i, scale=2)

        # save the image
        img_o.save("{}\\test_upscaler_{}.png".format(
            file_path, method), format="png")
        return True
    except Exception as e:
        print(e)
        return False


# test img2img
def test_img2img(prompt: str, method: Img2ImgMethod) -> bool:
    try:
        try:
            img_i = Image.open('{}\\test.png'.format(file_path))
        except FileNotFoundError:
            return False

        # convert the image
        img_o = Img2Img(method).run(img_i, prompt=prompt)

        # save the image
        img_o.save("{}\\test_img2img_{}.png".format(
            file_path, method), format="png")
        return True

    except Exception as e:
        print(e)
        return False


# test text2img
def test_text2img(prompt: str, method: Text2ImgMethod) -> bool:
    try:
        # convert the image
        img_o = Text2Img(method).run(prompt=prompt)

        # save the image
        img_o.save("{}\\test_text2img_{}.png".format(
            file_path, method), format="png")

        return True

    except Exception as e:
        print(e)
        return False


# test the uscaler class
if __name__ == "__main__":

    #assert tests
    prompt = "A gallery of paintings"

    # test img2img and all methods
    for method in Img2ImgMethod:
        assert test_img2img(prompt, method)

    # test text2img and all methods
    for method in Text2ImgMethod:
        assert test_text2img(prompt, method)

    # test upscaler and all methods
    for method in UpscalerMethod:
        assert test_upscaler(method)
