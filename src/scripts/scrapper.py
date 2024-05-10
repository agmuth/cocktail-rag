import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader

import os


documents = SimpleWebPageReader().load_data(
    # ["http://paulgraham.com/worked.html"]
    [
        "https://www.liquor.com/night-tripper-cocktail-recipe-8410923"
    ]
)

print(documents[0])
pass