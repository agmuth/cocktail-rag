from pathlib import Path, PosixPath
from typing import Any, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJ_DIR: PosixPath = Path(__file__).parent.parent
    DATA_DIR: Optional[str] = "data"
    PERSIST_DIR: Optional[str] = "storage"

    OLLAMA_HOST: str
    OLLAMA_PORT: int
    OLLAMA_LLM: str

    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_DB_NAME: str

    QDRANT_HOST: str
    QDRANT_PORT: int
    QDRANT_COLLECTION_NAME: str

    UI_HOST: str
    UI_PORT: int

    API_HOST: str
    API_PORT: int

    # uris -> constructed below
    OLLAMA_BASE_URL: Any = None
    MONGO_URI: Any = None
    QDRANT_URL: Any = None
    API_URL: Any = None

    def __init__(self):
        super().__init__()
        self.DATA_DIR: Path = self.PROJ_DIR.joinpath(self.DATA_DIR)
        self.PERSIST_DIR: Path = self.PROJ_DIR.joinpath(self.PERSIST_DIR)

        self.OLLAMA_BASE_URL: str = f"http://{self.OLLAMA_HOST}:{self.OLLAMA_PORT}"
        self.MONGO_URI: str = f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}"
        self.QDRANT_URL: str = f"http://{self.QDRANT_HOST}:{self.QDRANT_PORT}"
        self.API_URL: str = f"http://{self.API_HOST}:{self.API_PORT}"


BASE_SETTINGS = Settings()
