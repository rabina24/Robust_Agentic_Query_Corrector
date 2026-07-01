from groq import Groq
import json
import os
from agentic_query_corrector.agents.prompts import PROMPTS

os.environ["GROQ_API_KEY"] = "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"

class DetectorAgent:

    def __init__(self):

        self.client = Groq(api_key=os.environ["GROQ_API_KEY"])

    def detect(self, query):

        completion = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            temperature=0,
            response_format={"type":"json_object"},
            messages=[
                {
                    "role":"system",
                    "content":PROMPTS.DETECTOR_SYSTEM_PROMPT
                },
                {
                    "role":"user",
                    "content":PROMPTS.DETECTOR_USER_PROMPT.format(user_query=query)
                }
            ]
        )

        return json.loads(
            completion.choices[0].message.content
        )