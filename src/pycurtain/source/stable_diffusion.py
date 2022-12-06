import os
from typing import Generator, List
from PIL import Image
from random import randint
import warnings
from io import BytesIO
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
# local imports
import pycurtain.secrete.stuff as shh
from pycurtain.source.protos.image import TaskImage


global stability_api
stability_api = None


class StabilityAI(TaskImage):
    def __init__(self, api_key: str = None):

        self.api_key = api_key
        # get os environment variable deep_ai, raise exception if not found
        if api_key is None:
            api_key = os.environ.get(shh.STABILITY_AI_API_KEY)
            if api_key is None:
                raise Exception(
                    "Stabililty AI API KEY environment variable not found")

        # create a stability api client
        global stability_api
        stability_api = client.StabilityInference(
            key=api_key,
            verbose=True,
        )

    def generate(self, prompt: str, seed: int = None) -> List[Image.Image]:

        if prompt is None:
            raise Exception("Prompt cannot be None")

        if seed is None:
            seed = randint(0, 1000000)

        # create a request
        answers = stability_api.generate(
            prompt=prompt,
            sampler=generation.SAMPLER_K_DPM_2_ANCESTRAL,
            seed=seed,
            guidance_preset=generation.GUIDANCE_PRESET_SIMPLE,
            guidance_strength=0.5,
        )
        img_o = self.__download_img(answers)
        # wrap image in list
        return [img_o]

    def edit(self, prompt: str,  img_i: Image.Image, img_m: Image.Image, seed: int = None) -> List[Image.Image]:

        if prompt is None:
            raise Exception("Prompt cannot be None")

        if img_i is None:
            raise Exception("Image cannot be None")

        if img_m is None:
            raise Exception("Mask cannot be None")

        if seed is None:
            seed = randint(0, 1000000)

        # create a request
        answers = stability_api.generate(
            prompt=prompt,
            mask_image=img_m,
            init_image=img_i,
            sampler=generation.SAMPLER_K_DPM_2_ANCESTRAL,
            seed=seed,
            guidance_preset=generation.GUIDANCE_PRESET_SIMPLE,
            guidance_strength=0.75,
            start_schedule=0.7,
            end_schedule=0.01,
        )

        img_o = self.__download_img(answers)
        # wrap image in list
        return [img_o]

    def vary(self, prompt: str,  img_i: Image.Image, seed: int = None) -> List[Image.Image]:

        if prompt is None:
            raise Exception("Prompt cannot be None")

        if img_i is None:
            raise Exception("Image cannot be None")

        if seed is None:
            seed = randint(0, 1000000)

        # create a request
        answers = stability_api.generate(
            prompt=prompt,
            init_image=img_i,
            sampler=generation.SAMPLER_K_DPM_2_ANCESTRAL,
            seed=seed,
            guidance_preset=generation.GUIDANCE_PRESET_SIMPLE,
            guidance_strength=0.5,
            start_schedule=0.6,
            end_schedule=0.01,
        )

        img_o = self.__download_img(answers)
        # wrap image in list
        return [img_o]

    def __download_img(self, answers:  Generator[generation.Answer, None, None]) -> Image.Image:
        # iterating over the generator produces the api response
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(BytesIO(artifact.binary))
                    return img
        return None
