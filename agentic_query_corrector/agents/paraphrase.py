from agentic_query_corrector.llm import LocalLLM
from agentic_query_corrector.agents.prompts import PROMPTS

class ParaphraseAgent:

    def __init__(self):
        self.llm = LocalLLM()

    def correct(self, query):

        messages = [
            {"role":"system","content":PROMPTS.COMMON_SYSTEM_PROMPT},
            {"role":"user","content":PROMPTS.PARAPHRASE_PROMPT.format(user_query=query)}
        ]

        output = self.llm(messages)

        return output[0]["generated_text"][-1]["content"].strip()