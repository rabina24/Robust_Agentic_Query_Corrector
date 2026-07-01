import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import os
os.environ["HF_TOKEN"] = "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"
MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct"

class LocalLLM:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

            model = AutoModelForCausalLM.from_pretrained(
                MODEL_NAME,
                torch_dtype=torch.bfloat16,
                device_map="auto"
            )

            pipe = pipeline(
                "text-generation",
                model=model,
                tokenizer=tokenizer,
                max_new_tokens=64,
                do_sample=False
            )

            cls._instance = pipe

        return cls._instance