from llama_index.storage.docstore.mongodb import MongoDocumentStore

from src.settings import BASE_SETTINGS

document_store = MongoDocumentStore.from_uri(
    uri=BASE_SETTINGS.MONGO_URI, db_name=BASE_SETTINGS.MONGO_DB_NAME
)
