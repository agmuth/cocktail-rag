from typing import Optional

import typer
from typing_extensions import Annotated

from src.rag.components.loader import loader
from src.rag.components.pipeline import pipeline


def main(num_files_limit: Annotated[Optional[int], typer.Argument()] = None):
    if num_files_limit and isinstance(num_files_limit, int):
        loader.num_files_limit = num_files_limit
        loader.input_files = loader._add_files(loader.input_dir)

    documents = loader.load_data(show_progress=True)
    pipeline.run(documents=documents, show_progress=True)


if __name__ == "__main__":
    typer.run(main)
    
    
