from typing import Optional

import typer

from src.rag.components.loader import loader
from src.rag.components.pipeline import pipeline


def main(num_files_limit: Optional[int] = None):
    if num_files_limit and isinstance(num_files_limit, int):
        loader.num_files_limit = num_files_limit

    documents = loader.load_data(show_progress=True)
    _ = pipeline.run(documents=documents, show_progress=True)


if __name__ == "__main__":
    typer.run(main)
