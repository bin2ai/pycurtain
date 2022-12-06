import datetime
import os
from typing import List, Tuple
import openai
from transformers import GPT2Tokenizer
# local imports
import pycurtain.secrete.stuff as shh
from pycurtain.source.protos.text import TaskText


class GPT3(TaskText):
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.environ.get(shh.OPENAI_API_KEY)
            if self.api_key is None:
                raise Exception(
                    "OPENAI API KEY environment variable not found")
        openai.api_key = os.getenv(self.api_key)
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # summarize prompt

    def summarize(self, prompt: str, max_tokens_res: int = 100) -> str:
        # split prompt into chunks no more than 1000 tokens
        prompt_chunks = self.__split_text_by_tokens(
            prompt, 4000-max_tokens_res)
        # summarize each chunk
        summaries = []
        for chunk in prompt_chunks:
            summaries.append(self.__summarize(chunk, max_tokens_res))
        # join summaries
        summary = " ".join(summaries)
        return summary

    # summarize prompt

    def __summarize(self, prompt: str, max_tokens: int = 100):

        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="{}\n\ntl;dr".format(prompt),
            max_tokens=max_tokens,
            temperature=0
        )

        return self.__parse_completion(res)

    # fix grammar from prompt

    def fix_grammar(self, prompt: str, max_tokens_res: int = 2000) -> str:
        # split prompt into chunks no more than 1000 tokens
        prompt_chunks = self.__split_text_by_tokens(
            prompt, 4000-max_tokens_res)
        # fix grammar for each chunk
        text = []
        for chunk in prompt_chunks:
            text.append(self.__fix_grammar(chunk, max_tokens_res))
        # join summaries
        summary = " ".join(text)
        return summary

    # fix grammar from prompt

    def __fix_grammar(self, prompt: str, max_tokens: int = 100) -> str:
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="{}\n\nfix the spelling errors.".format(prompt),
            max_tokens=max_tokens,
            temperature=0
        )

        return self.__parse_completion(res)

    # list gpt models

    def __list_models_by_date():

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

    # convert prompt to tags

    def tag(self, prompt: str, max_tokens: int = 100) -> List[Tuple[str, str]]:
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="list tags about subject\ni.e.\nsubject: apples\ntags: food, fruit, red, juicy, healthy, tart, crunchy, pies, cider, juice, snacks, pie, dessert\nsubject: {}\ntags:\n".format(
                prompt),
            max_tokens=max_tokens,
            temperature=0
        )

        return self.__parse_completion(res)

    def __parse_completion(self, res) -> str:
        task_type = res["object"]
        created_ts = res["created"]
        choices = res["choices"]

        text = []
        for choice in choices:
            text.append(choice["text"])
            choice["finish_reason"]

        usage = res["usage"]
        prompt_tokens = usage["prompt_tokens"]
        completion_tokens = usage["completion_tokens"]
        total_tokens = usage["total_tokens"]
        return " ".join(text)

    def __text_to_tokens(self, text: str) -> int:
        return self.tokenizer(text)['input_ids']

    def __split_text_by_tokens(self, text: str, size: int) -> List[str]:
        tokens = self.__text_to_tokens(text)
        lst = []
        tmp = []
        # create list of lists where each sublist is no more than size tokens
        for token in tokens:
            tmp.append(token)
            if len(tmp) >= size:
                lst.append(tmp)
                tmp = []
        if len(tmp) > 0:
            lst.append(tmp)
        # convert each sublist to text
        lst = [self.tokenizer.decode(x) for x in lst]
        return lst
