from typing import List
from PIL import Image, ImageDraw
# local imports
import pycurtain.source as Source
from pycurtain.task import Image as Image_AI


# test task\image\__init__.py generate
def test_generate(source_type: Source.SourceImageType):
    # arrange
    prompt = "test"
    img_o_lst = Image_AI(source_type).generate(prompt)
    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_generate_" +
                   str(i) + str(source_type) + ".png")
    # assert
    assert img_o_lst is not None


# test task\image\__init__.py edit
def test_edit(source_type: Source.SourceImageType):
    # arrange
    prompt = "a lab experiment test"
    img_i = Image.open("tests\\test.png")
    # create circle mask
    img_m = Image.new("L", img_i.size, 0)
    draw = ImageDraw.Draw(img_m)
    draw.ellipse((0, 0) + img_m.size, fill=255)

    # act
    img_o_lst: List[Image.Image] = Image_AI(source_type).edit(prompt=prompt,
                                                              img_i=img_i, img_m=img_m)
    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_edit_" +
                   str(i) + str(source_type) + ".png")
    # assert
    assert img_o_lst is not None


# test task\image\__init__.py vary
def test_vary(source_type: Source.SourceImageType):
    # arrange
    prompt = "test"
    img_i = Image.open("tests\\test.png")
    source = Source.SourceImage(source_type=source_type)
    # act
    img_o_lst = Image_AI(source_type).vary(prompt=prompt, img_i=img_i)

    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_vary_" +
                   str(i) + str(source_type) + ".png")

    # assert
    assert img_o_lst is not None


# test task\image\__init__.py upscale
def test_upscale(source_type: Source.SourceImageType):
    # arrange
    img_i = Image.open("tests\\test.png")
    source = Source.SourceImage(source_type=source_type)
    # act
    img_o_lst = Image_AI.upscale(source, img_i)

    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_upscale_" +
                   str(i) + str(source_type) + ".png")

    # assert
    assert img_o is not None


# main
if __name__ == "__main__":

    # assert tests for all valid source types
    # test_generate(Source.SourceImageType.STABLE_DIFFUSION)
    # test_generate(Source.SourceImageType.DALLE2)
    # mask = create_circle_mask((512, 512)).save("tests\\test_001_mask.png")
    # test_edit(Source.SourceType.STABLE_DIFFUSION)
    # test_edit(Source.SourceType.DALLE2)
    # test_vary(Source.SourceType.STABLE_DIFFUSION)
    # test_vary(Source.SourceType.DALLE2)
    # test_upscale(Source.SourceType.DEEP_AI)
    # test_generate(Source.SourceType.CRAIYON)

    # test replicate
    # test_generate(Source.SourceImageType.REPLICATE)
    # test_edit(Source.SourceImageType.REPLICATE)
    test_vary(Source.SourceImageType.REPLICATE)

    pass
