import pycurtain

from PIL import Image

if __name__ == "__main__":

    import numpy as np

    print("Testing Stability AI")

    # test edit
    task = pycurtain.task.Image(
        pycurtain.task.SourceImageType.STABLE_DIFFUSION)

    img_i = Image.open("tests\\test.png")
    img_i.show()

    # np array 512x512 all white
    mask = np.ones((512, 512, 3), np.uint8) * 255

    # right is black from position 256,0 to 512,512
    mask[0:512, 256:512] = (0, 0, 0)
    img_m = Image.fromarray(mask)

    img_m.show()

    print("Testing edit")

    prompt = 'a galaxy in space'
    img_o = task.edit(img_i=img_i,
                      img_m=img_m,
                      prompt=prompt)[0]
    img_o.show()
    img_o.save("test_out.png")
