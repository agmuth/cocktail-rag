import os.path

from llama_index.core import (SimpleDirectoryReader, StorageContext,
                              VectorStoreIndex, load_index_from_storage)
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

from settings import BASE_SETTINGS

llm = Ollama(model="phi", request_timeout=60 * 2)
embed_model = OllamaEmbedding("phi")

# check if storage already exists
if not os.path.exists(BASE_SETTINGS.PERSIST_DIR):
    # load the documents and create the index
    loader = SimpleDirectoryReader(
        input_dir=BASE_SETTINGS.DATA_DIR,
        recursive=True,
    )
    documents = loader.load_data(show_progress=True)

    from random import sample

    n = 100
    documents = sample(documents, n)

    index = VectorStoreIndex.from_documents(
        documents,
        embed_model=embed_model,
        show_progress=True,
    )
    # store it for later
    index.storage_context.persist(persist_dir=BASE_SETTINGS.PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(
        persist_dir=BASE_SETTINGS.PERSIST_DIR,
    )
    index = load_index_from_storage(storage_context)


query_engine = index.as_query_engine(llm=llm)

query = "Please recommend me a Fancy cocktail. Include a list of ingredients and instructions for how to make it."
response = query_engine.query(query)
print(response)
#  RAG response:
# -----------------------------------------------------------------------------------------------------------------------------------------------
#   A Fancy Cocktail is a sophisticated drink that is perfect for special occasions or as a treat for yourself. Here's an example of one:
#   Name: Flaming Pina Colada
#   Ingredients:
#   - 1 can (12 oz) canned pineapple chunks
#   - 2 cups light rum
#   - 1 cup coconut cream
#   - 2 scoops vanilla ice cream
#   - 1/2 cup dark crème de cacao
#   - 1/4 cup lime juice
#   - 1 teaspoon sugar
#   - 1/4 teaspoon salt
#   Instructions:
#   1. In a blender, combine the pineapple chunks, light rum, coconut cream, ice cream, dark creme de cacao, lime juice, sugar, and salt. Blend until smooth.
#   2. Pour into a tall glass filled with crushed ice.
#   3. If desired, add a straw and a cherry on top for garnish.
#   Summary: The Flaming Pina Colada is a classic cocktail that features a combination of sweet and spicy flavors. It's perfect for a tropical-themed party or as a special treat at home. Enjoy responsibly!
#   You may use different variations of the same ingredient, such as using coconut milk instead of cream in this recipe. Have fun experimenting with your own creations!
