# ref: https://sharmadave.medium.com/llama-index-unleashes-the-power-of-chatgpt-over-your-own-data-b67cc2e4e277

import time

import gradio as gr

from src.rag.components.chat_engine import \
    chat_engine  # TODO: move chat enginge to behind fastapi

# def main():
with gr.Blocks() as demo:

    chatbot = gr.Chatbot()
    msg = gr.Textbox(
        label="⏎ for sending",
        placeholder="Ask me something",
    )
    clear = gr.Button("Delete")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        user_message = history[-1][0]
        bot_message = chat_engine.chat(user_message)
        history[-1][1] = ""
        for character in bot_message.response:
            history[-1][1] += character
            time.sleep(0.01)
            yield history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=True).then(
        bot, chatbot, chatbot
    )

    clear.click(lambda: None, None, chatbot, queue=True)

demo.queue().launch(debug=True, server_name="0.0.0.0", server_port=7860, share=False)
# .launch(server_name=BASE_SETTINGS.GRADIO_SERVER_NAME, server_port=BASE_SETTINGS.GRADIO_SERVER_PORT)


# if __name__ == "__main__":
#     typer.run(main)
