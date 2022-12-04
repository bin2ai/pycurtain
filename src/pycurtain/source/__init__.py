from enum import Enum
# local imports
from pycurtain.source.craiyon import Craiyon
from pycurtain.source.dalle2 import DALLE2
from pycurtain.source.deep_ai import DeepAI
from pycurtain.source.gpt3 import GPT3
from pycurtain.source.stable_diffusion import StabilityAI


class SourceType(Enum):
    STABLE_DIFFUSION = 0
    DEEP_AI = 1
    DALLE2 = 2
    CRAIYON = 3
    GPT3 = 4


class Source_AI():
    def __init__(self, source_type: SourceType, api_key: str = None):
        self.source_type = source_type
        self.api_key = api_key
        if source_type == SourceType.STABLE_DIFFUSION:
            self.source = StabilityAI(api_key)
        elif source_type == SourceType.DALLE2:
            self.source = DALLE2(api_key)
        elif source_type == SourceType.DEEP_AI:
            self.source = DeepAI(api_key)
        elif source_type == SourceType.CRAIYON:
            self.source = Craiyon()
        elif source_type == SourceType.GPT3:
            self.source = GPT3(api_key)
        else:
            raise Exception("Invalid source type")
