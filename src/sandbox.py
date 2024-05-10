# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
# from llama_index.llms.huggingface import HuggingFaceLLM

# documents = SimpleDirectoryReader("./data").load_data()
# documents = documents[:10]

# from llama_index.core import PromptTemplate

# system_prompt = """<|SYSTEM|>#
# Mistral Research is an expert in the field of research
# """

# # This will wrap the default prompts that are internal to llama-index
# query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")

# import torch

# llm = HuggingFaceLLM(
#     context_window=4096,
#     max_new_tokens=256,
#     generate_kwargs={"temperature": 0, "do_sample": False},
#     system_prompt=system_prompt,
#     query_wrapper_prompt=query_wrapper_prompt,
#     tokenizer_name="mistralai/Mistral-7B-v0.1",
#     model_name="mistralai/Mistral-7B-v0.1",
#     device_map="auto",
#     tokenizer_kwargs={"max_length": 4096},
#     # uncomment this if using CUDA to reduce memory usage
#     model_kwargs={
#         "torch_dtype": torch.float16, 
#         "llm_int8_enable_fp32_cpu_offload": True,
#         "bnb_4bit_quant_type": 'nf4',
#         "bnb_4bit_use_double_quant":True,
#         "bnb_4bit_compute_dtype":torch.bfloat16,
#         "load_in_4bit": True}
# )

# service_context = ServiceContext.from_defaults(chunk_size=1024,
#                                                llm=llm,
#                                                embed_model='local')


# index = VectorStoreIndex.from_documents(
#     documents, service_context=service_context
# )

# query_engine = index.as_query_engine(streaming=True)

# response_stream = query_engine.query("How do you make a 007 cocktail?")
# response_stream.print_response_stream()


from llama_index.llms.ollama import Ollama
llm = Ollama(model="llama2", request_timeout=300.0)
resp = llm.complete("ping")
print(resp)