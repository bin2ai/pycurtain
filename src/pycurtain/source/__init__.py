from enum import Enum
# local imports
from pycurtain.source.craiyon import Craiyon
from pycurtain.source.dalle2 import DALLE2
from pycurtain.source.deep_ai import DeepAI
from pycurtain.source.gpt3 import GPT3
from pycurtain.source.replicate_stable_diffusion import ReplicateStableDiffusion
from pycurtain.source.stable_diffusion import StabilityAI


class SourceImageType(Enum):
    STABLE_DIFFUSION = 0
    DEEP_AI = 1
    DALLE2 = 2
    CRAIYON = 3
    REPLICATE = 4


class SourceImage():
    def __init__(self, source_type: SourceImageType, api_key: str = None):
        self.source_type = source_type
        self.api_key = api_key
        if source_type == SourceImageType.STABLE_DIFFUSION:
            self.source = StabilityAI(api_key)
        elif source_type == SourceImageType.DALLE2:
            self.source = DALLE2(api_key)
        elif source_type == SourceImageType.DEEP_AI:
            self.source = DeepAI(api_key)
        elif source_type == SourceImageType.CRAIYON:
            self.source = Craiyon()
        elif source_type == SourceImageType.REPLICATE:
            self.source = ReplicateStableDiffusion(api_key)
        else:
            raise Exception("Invalid source type")


class SourceTextType(Enum):
    GPT3 = 0


class SourceText():
    def __init__(self, source_type: SourceTextType, api_key: str = None):
        self.source_type = source_type
        self.api_key = api_key
        if source_type == SourceTextType.GPT3:
            self.source = GPT3(api_key)
        else:
            raise Exception("Invalid source type")
