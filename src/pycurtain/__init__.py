from pycurtain import task as task
from pycurtain import source as source
from pycurtain import utility as utility
from pycurtain import secrete as secrete
from pycurtain import process as process


# list all sources
def list_sources():
    dic = {}
    dic["image"] = source.list_sourceImage_types()
    dic["text"] = source.list_sourceText_types()
    return dic


def list_tasks():
    dic = {}
    dic["image"] = task.list_image_tasks()
    dic["text"] = task.list_text_tasks()
    return dic
