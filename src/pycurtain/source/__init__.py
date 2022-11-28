from enum import Enum
# local imports
import pycurtain.source.dalle2 as dalle2
import pycurtain.source.stable_diffusion as stable_diffusion
import pycurtain.source.deep_ai as deep_ai


class SourceType(Enum):
    STABLE_DIFFUSION = 0
    DEEP_AI = 1
    DALLE2 = 2


class Source_AI():
    def __init__(self, source_type: SourceType, api_key: str = None):
        self.source_type = source_type
        self.api_key = api_key
        if source_type == SourceType.STABLE_DIFFUSION:
            self.source = stable_diffusion.StabilityAI(api_key)
        elif source_type == SourceType.DALLE2:
            self.source = dalle2.DALLE2(api_key)
        elif source_type == SourceType.DEEP_AI:
            self.source = deep_ai.DeepAI(api_key)
        else:
            raise Exception("Invalid source type")
