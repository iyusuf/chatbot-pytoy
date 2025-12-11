import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Hello from Chainlit! 🎉").send()


@cl.on_message
async def on_message(message: cl.Message):
    reply = f"You said: {message.content}"
    await cl.Message(content=reply).send()

