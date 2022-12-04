from PIL import Image, ImageDraw
import pycurtain.source as Source
import pycurtain.task.image as Image_AI


# test task\image\__init__.py generate
def test_generate(source_type: Source.SourceType):
    # arrange
    prompt = "test"
    source = Source.Source_AI(source_type=source_type)
    # act
    img_o_lst = Image_AI.generate(source, prompt)
    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_generate_" +
                   str(i) + str(source_type) + ".png")
    # assert
    assert img_o_lst is not None


# test task\image\__init__.py edit
def test_edit(source_type: Source.SourceType):
    # arrange
    prompt = "a lab experiment test"
    img_i = Image.open("tests\\test_001.png")
    img_m = Image.open("tests\\test_001_mask.png")
    source = Source.Source_AI(source_type=source_type)
    # act
    img_o_lst = Image_AI.edit(source=source, prompt=prompt,
                              img_i=img_i, img_m=img_m)
    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_edit_" +
                   str(i) + str(source_type) + ".png")
    # assert
    assert img_o_lst is not None


# test task\image\__init__.py vary
def test_vary(source_type: Source.SourceType):
    # arrange
    prompt = "test"
    img_i = Image.open("tests\\test.png")
    source = Source.Source_AI(source_type=source_type)
    # act
    img_o_lst = Image_AI.vary(source=source, prompt=prompt, img_i=img_i)

    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_vary_" +
                   str(i) + str(source_type) + ".png")

    # assert
    assert img_o_lst is not None


# test task\image\__init__.py upscale
def test_upscale(source_type: Source.SourceType):
    # arrange
    img_i = Image.open("tests\\test.png")
    source = Source.Source_AI(source_type=source_type)
    # act
    img_o_lst = Image_AI.upscale(source, img_i)

    for i, img_o in enumerate(img_o_lst):
        # save image as rgba png
        img_o.save("tests\\test_001_upscale_" +
                   str(i) + str(source_type) + ".png")

    # assert
    assert img_o is not None


# create a circle mask
def create_circle_mask(size: tuple) -> Image.Image:
    img_o = Image.new('L', size, 0)
    draw = ImageDraw.Draw(img_o)
    draw.ellipse((0, 0) + size, fill=255)
    # invert the mask
    # img_o = invert(img_o)
    # transparent the mask
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


# main
if __name__ == "__main__":

    # assert tests for all valid source types
    # test_generate(Source.SourceType.STABLE_DIFFUSION)
    # test_generate(Source.SourceType.DALLE2)
    # mask = create_circle_mask((512, 512)).save("tests\\test_001_mask.png")
    # test_edit(Source.SourceType.STABLE_DIFFUSION)
    # test_edit(Source.SourceType.DALLE2)
    # test_vary(Source.SourceType.STABLE_DIFFUSION)
    # test_vary(Source.SourceType.DALLE2)
    # test_upscale(Source.SourceType.DEEP_AI)

    # test_generate(Source.SourceType.CRAIYON)
    # test text summarize
    pass
