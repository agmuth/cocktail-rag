import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import Settings

import tiktoken
# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

from transformers import AutoTokenizer

Settings.tokenizer = AutoTokenizer.from_pretrained(
    "HuggingFaceH4/zephyr-7b-beta"
)

# load documents
documents = SimpleDirectoryReader("./data/paul_graham/").load_data()

# setup prompts - specific to StableLM
from llama_index.core import PromptTemplate

# This will wrap the default prompts that are internal to llama-index
# taken from https://huggingface.co/Writer/camel-5b-hf
query_wrapper_prompt = PromptTemplate(
    "Below is an instruction that describes a task. "
    "Write a response that appropriately completes the request.\n\n"
    "### Instruction:\n{query_str}\n\n### Response:"
)

import torch

llm = HuggingFaceLLM(
    context_window=2048,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.25, "do_sample": False},
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="HuggingFaceH4/zephyr-7b-beta",
    model_name="HuggingFaceH4/zephyr-7b-beta",
    device_map="auto",
    tokenizer_kwargs={"max_length": 2048},
    # uncomment this if using CUDA to reduce memory usage
    model_kwargs={"torch_dtype": torch.float16}
)

Settings.chunk_size = 512
Settings.llm = llm

index = VectorStoreIndex.from_documents(documents)

# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)