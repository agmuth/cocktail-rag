from pathlib import Path, PosixPath

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATA_DIR: str
    PERSIST_DIR: str
    PROJ_DIR: PosixPath = Path(__file__).parent.parent

    def __init__(self):
        super().__init__()

        self.DATA_DIR = self.PROJ_DIR.joinpath(self.DATA_DIR)
        if not self.DATA_DIR.exists():
            self.DATA_DIR.mkdir()

        self.PERSIST_DIR = self.PROJ_DIR.joinpath(self.PERSIST_DIR)


BASE_SETTINGS = Settings()
