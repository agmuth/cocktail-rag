from textwrap import dedent

from src.rag.components.query_engine import query_engine

txt = dedent(
    """
    Recommend me a fun cocktail!
    """.strip()
)
response = query_engine.query(txt)
print(response)
