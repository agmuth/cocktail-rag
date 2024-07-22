from src.rag.components.vector_store import vector_store

from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate
from llama_index.core import VectorStoreIndex
from llama_index.core import VectorStoreIndex

from src.rag.components.embed_model import embed_model
from src.rag.components.llm import llm
from src.rag.components.vector_store import vector_store


qa_prompt_str = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the question: {query_str}\n"
)
# Text QA Prompt
chat_text_qa_msgs = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=(
            "Always answer the question, even if the context isn't helpful."
        ),
    ),
    ChatMessage(role=MessageRole.USER, content=qa_prompt_str),
]
text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)


chat_engine = (
    VectorStoreIndex.
    from_vector_store(
        vector_store=vector_store, embed_model=embed_model
    )
    .as_chat_engine(llm=llm, text_qa_template=text_qa_template,)
)

