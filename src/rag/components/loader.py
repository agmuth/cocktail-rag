from llama_index.core import SimpleDirectoryReader

from src.settings import BASE_SETTINGS

loader = SimpleDirectoryReader(
    input_dir=BASE_SETTINGS.DATA_DIR,
    recursive=True,
    required_exts=[".txt"],
    filename_as_id=True,
)
