import os
from PIL import Image
from random import randint
import warnings
from io import BytesIO

from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# local imports
from pycurtain.text2img.template import Text2Img
import pycurtain.secrete.stuff as shh


global stability_api
stability_api = None


class StabilityAI(Text2Img):
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

    def run(self, prompt: str, img_i: Image.Image = None, img_m: Image.Image = None, seed: int = None) -> Image.Image:
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
            guidance_strength=0.5,
            start_schedule=0.9,
            end_schedule=0.01,
        )

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
