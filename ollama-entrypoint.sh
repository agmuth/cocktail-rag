#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

echo "🔴 🔴 🔴 Waiting for Ollama server to be active..."
while [ "$(ollama list | grep 'NAME')" == "" ]; do
    sleep 1
done
echo "🟢 🟢 🟢 Ollama server active."

echo "🔴 🔴 🔴 Pulling model..."
ollama pull ${OLLAMA_LLM}
echo "🟢 🟢 🟢 Model pulled."

echo "🔴 🔴 🔴 Starting model..."
# ollama run phi & /bye
ollama run ${OLLAMA_LLM} ""
echo "🟢 🟢 🟢 Model started."

# Wait for Ollama process to finish.
wait $pid