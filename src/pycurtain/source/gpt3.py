import datetime
import os
from typing import List, Tuple
import openai


class GPT3():
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.environ.get("OPENAI_API_KEY")
            if self.api_key is None:
                raise Exception(
                    "OPENAI API KEY environment variable not found")
        openai.api_key = os.getenv("OPENAI_API_KEY")

    # summarize prompt
    def summarize(self, prompt: str, max_tokens: int = 100):

        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="{}\n\ntl;dr".format(prompt),
            max_tokens=100,
            temperature=0
        )

        return self.__parse_completion(res)

    # fix grammar from prompt
    def fix_grammar(self, prompt: str, max_tokens: int = 100) -> str:
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="{}\n\nfix the spelling errors.".format(prompt),
            max_tokens=1000,
            temperature=0
        )

        return self.__parse_completion(res)

    # list gpt models

    def list_models_by_date():

        models = openai.Model.list()['data']

        ts_ids = {}

        for model in models:
            id = model["id"]
            created = model["created"]
            # timestamp to datetime
            created = datetime.datetime.fromtimestamp(created)
            # print("{} {}".format(id, created))
            ts_ids[created] = id

        # sort by timestamp
        ts_ids = dict(sorted(ts_ids.items(), key=lambda item: item[0]))
        return ts_ids

    def tag(self, prompt: str, max_tokens: int = 100) -> List[Tuple[str, str]]:
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="List tags relating to subject, genre, subgenre, etc.{}\n\n:".format(
                prompt),
            max_tokens=max_tokens,
            temperature=0
        )

        return self.__parse_completion(res)

    def __parse_completion(self, res):
        task_type = res["object"]
        created_ts = res["created"]
        choices = res["choices"]

        text = []
        for choice in choices:
            text.append((choice["text"]))
            choice["finish_reason"]
        usage = res["usage"]
        prompt_tokens = usage["prompt_tokens"]
        completion_tokens = usage["completion_tokens"]
        total_tokens = usage["total_tokens"]

        return "".join(text)
