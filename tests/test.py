

if __name__ == "__main__":

    try:
        import pycurtain
        assert True, "pycurtain installed"
    except ImportError:
        assert False, "pycurtain not installed"

    print("list all available sources")
    print(pycurtain.list_sources())
    print("list all available tasks")
    print(pycurtain.list_tasks())

    # test
    # set source to image craiyon
    source = pycurtain.source.SourceImageType.CRAIYON
    # set task to generate
    task = pycurtain.task.Image(source)
    # set prompt
    prompt = "a wonderful day"
    # generate image
    img = task.generate(prompt=prompt)
    # save image
    img[0].save("test.png")
