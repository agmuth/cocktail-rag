from pathlib import Path, PosixPath
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJ_DIR: PosixPath = Path(__file__).parent.parent
    DATA_DIR: str = "data"
    PERSIST_DIR: str = "storage"

    OLLAMA_LLM: str = "phi"
    OLLAMA_HOST: str = "localhost"
    OLLAMA_PORT: int = 11434

    MONGO_INITDB_ROOT_USERNAME: str = "root"
    MONGO_INITDB_ROOT_PASSWORD: str = "example"
    MONGO_PORT: int = 27017
    MONGO_HOST: str = "localhost"
    MONGO_URI: Optional[str] = None

    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333

    def __init__(self):
        super().__init__()
        self.DATA_DIR = self.PROJ_DIR.joinpath(self.DATA_DIR)
        self.PERSIST_DIR = self.PROJ_DIR.joinpath(self.PERSIST_DIR)
        self.MONGO_URI = f"mongodb://{self.MONGO_INITDB_ROOT_USERNAME}:{self.MONGO_INITDB_ROOT_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}"


BASE_SETTINGS = Settings()
