import pycurtain.process.text_to_video_zoom as text_to_video_zoom
from pycurtain.source import SourceImageType


# test text_to_video_zoom_in
def test_zoom_in():

    prompt = "1970s, classic rock, retro, music, roses, guitar, colorful, arstic, high detailed, masterpiece, drawing, epic grateful dead poster, from Rick Griffin, with skeletons amid roses, with swords and a giant skull in the background.  No words or text displayed"
    text_to_video_zoom.zoom_in(
        prompts=[prompt], source=SourceImageType.STABLE_DIFFUSION, n_imgs=10, file_name="text-to-video-zoom.mp4")


if __name__ == "__main__":
    test_zoom_in()
