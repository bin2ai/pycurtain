from typing import List
from PIL import Image
import imageio as imageio
import numpy as np
# local imports
from pycurtain.task import Image as Image_AI
from pycurtain.source import SourceImageType
from pycurtain.utility import image as ImageUtility
from pycurtain.utility.video import reverse_video


# function to generate a list of images using list of prompts, prompts repeat if n_imgs > len(prompts)
def __generate_zoom_img_list(prompts: List[str], n_imgs: int, source_type: SourceImageType) -> List[Image.Image]:
    img_ai = Image_AI(source=source_type)
    imgs = []
    img = img_ai.generate(prompts[0])[0]
    for i in range(n_imgs):
        prompt = prompts[i % len(prompts)]
        crop = ImageUtility.crop_in_by_factor(img, 2)
        mask = ImageUtility.create_mask_from_transparent(crop)
        img = img_ai.edit(prompt=prompt, img_i=crop,
                          img_m=mask)[0]
        imgs.append(img)
    return imgs


# function to generate a video from a list of images
def __zoom_imgs_to_video(imgs: List[Image.Image], transition_seconds: int = 4, fps: int = 64, flip_order=False, file_name: str = "output.mp4") -> None:

    if flip_order:
        # flip sequence order of images
        imgs = imgs[::-1]

    # frames per transition
    fpt = transition_seconds * fps
    with imageio.get_writer(file_name, mode="I", fps=fps) as writer:
        for img in imgs:
            # next image, if img is last image, break
            if imgs.index(img) == len(imgs) - 1:
                break
            # zoom in img
            for frame in range(fpt):
                o_img = ImageUtility.zoom_at(img, frame//2)
                writer.append_data(np.array(o_img))
        writer.append_data(np.array(img))


# function to generate a video from a list of prompts, prompts repeat if n_imgs > len(prompts)
def zoom_in(prompts: List[str], source: SourceImageType, n_imgs: int, file_name: str = "output.mp4") -> None:
    imgs = __generate_zoom_img_list(
        prompts=prompts, n_imgs=n_imgs, source_type=source)
    __zoom_imgs_to_video(imgs=imgs, flip_order=True, file_name=file_name)


def zoom_out(prompts: List[str], source: SourceImageType, n_imgs: int, file_name: str = "output.mp4") -> None:
    imgs = __generate_zoom_img_list(
        prompts=prompts, n_imgs=n_imgs, source_type=source)
    __zoom_imgs_to_video(imgs=imgs, flip_order=True, file_name=file_name)
    reverse_video(file_name)


if __name__ == "__main__":
    prompt = "1970s, classic rock, retro, music, roses, guitar, colorful, arstic, high detailed, masterpiece, drawing, epic grateful dead poster, from Rick Griffin, with skeletons amid roses, with swords and a giant skull in the background.  No words or text displayed"
