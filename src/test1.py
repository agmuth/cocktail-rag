import requests


# curl -X POST http://localhost:11434/api/generate -d '{
#   "model": "llama2",
#   "prompt":"Why is the sky blue?"
#  }'
 
 
url = "http://localhost:11434/api/generate"
payload = {
        "model": "phi",
        "prompt":"Why is the sky blue?"
    }

resp = requests.get(url, data=payload)
print(resp)
