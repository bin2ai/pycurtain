from typing import List
import requests
from PIL import Image
# local imports
from pycurtain.utility.image import base64_to_pil
from pycurtain.source.protos.image import TaskImage


class Craiyon(TaskImage):
    def __init__(self):
        pass

    def __generate(self):
        url = 'https://backend.craiyon.com/generate'
        headers = {
            'accept': '*/*',
            'access-control-request-headers': 'content-type',
            'access-control-request-method': 'POST',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/',
            'origin': 'https://www.craiyon.com',
        }
        response = requests.options(url, headers=headers)

    def generate(self, prompt: str) -> List[Image.Image]:
        self.__generate()
        url = 'https://backend.craiyon.com/generate'
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/',
        }

        data = '{"prompt": "' + prompt + '"}'
        response = requests.post(url, headers=headers, data=data)

        if response.status_code != 200:
            raise Exception(
                'Craiyon API error status_code: {}'.format(response.status_code))
        data = response.json()
        images = data['images']

        # version = response.json()['version']

        return [base64_to_pil(img) for img in images]
