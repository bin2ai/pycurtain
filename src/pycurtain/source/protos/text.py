class TaskText():

    api_key: str = None

    def __init__(self) -> None:
        # raise exception if this function is not overriden
        raise Exception(
            "__init__() function not implemented for this SourceTextType")

    def summarize(self, prompt: str) -> str:
        # raise exception if this function is not overriden
        raise Exception(
            "summarize() function not implemented for this SourceTextType")

    def fix_grammar(self, prompt: str) -> str:
        # raise exception if this function is not overriden
        raise Exception(
            "fix_grammar() function not implemented for this SourceTextType")

    def tag(self, prompt: str) -> str:
        # raise exception if this function is not overriden
        raise Exception(
            "tag() function not implemented for this SourceTextType")
