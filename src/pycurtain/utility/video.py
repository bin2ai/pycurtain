import imageio


# using numpy and imageio reverse the video
def reverse_video(file_name: str):
    reader = imageio.get_reader(file_name)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(
        file_name.replace(".mp4", "-reversed.mp4"), fps=fps)

    n_frames = 0
    imgs = []
    for i, im in enumerate(reader):
        imgs.append(im)
        n_frames += 1

    # reverse video
    for i in range(n_frames):
        writer.append_data(imgs[n_frames - i - 1])
    writer.close()
