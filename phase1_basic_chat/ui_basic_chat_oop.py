import chainlit as cl

from basic_chat_oop import BasicChatBot


bot = BasicChatBot()


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content=(
            "Hi, I'm your law-focused assistant. "
            "Ask me law-related questions. "
            "If you ask about something else, I will say 'i DONT KNOW'."
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    # Use the BasicChatBot to generate a response
    reply = bot.chat(message.content)
    await cl.Message(content=reply).send()

