from pycurtain.source import Source_AI, SourceType


def summarize(source: Source_AI, prompt: str, max_tokens_res: int) -> str:
    if source.source_type == SourceType.GPT3:
        return source.source.summarize(prompt=prompt, max_tokens_res=max_tokens_res)
    else:
        raise Exception("Invalid source type")


def fix_grammar(source: Source_AI, prompt: str) -> str:
    if source.source_type == SourceType.GPT3:
        return source.source.fix_grammar(prompt=prompt)
    else:
        raise Exception("Invalid source type")


def tag(source: Source_AI, prompt: str) -> str:
    if source.source_type == SourceType.GPT3:
        return source.source.tag(prompt=prompt)
    else:
        raise Exception("Invalid source type")
