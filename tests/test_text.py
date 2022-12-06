# test task text summarize

import pycurtain.source as Source
import pycurtain.task.text as Text_AI


def summarize(prompt: str, max_tokens: int = 100):
    # arrange
    source = Source.SourceImage(source_type=Source.SourceImageType.GPT3)
    # act
    res = Text_AI.summarize(source, prompt, max_tokens)
    # assert
    assert res is not None
    return res

# test task text fix_grammar


def fix_grammar(prompt: str):
    # arrange
    source = Source.SourceImage(source_type=Source.SourceImageType.GPT3)
    # act
    res = Text_AI.fix_grammar(source, prompt)
    # assert
    assert res is not None
    return res


def tag(prompt: str):
    # arrange
    source = Source.SourceImage(source_type=Source.SourceImageType.GPT3)
    # act
    res = Text_AI.tag(source, prompt)
    # assert
    assert res is not None
    return res


if __name__ == "__main__":
    # print(summarize("I am a sam, sam i am, i do not like green eggs and ham"))
    # print(fix_grammar("I am a sam, sam i am, i do not like green eggs and ham"))
    # print(tag("I am a sam, sam i am, i do not like green eggs and ham"))
    pass
