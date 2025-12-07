import chainlit as cl
from basic_chat_oop import BasicChatBot

@cl.on_chat_start
def start():
    """
    Instantiate the bot and store it in the user session.
    """
    bot = BasicChatBot()
    cl.user_session.set("bot", bot)

@cl.on_message
async def main(message: cl.Message):
    """
    Receive a message from the user, pass it to the bot, and send back the response.
    """
    bot = cl.user_session.get("bot")
    
    # Run the blocking bot.chat() call. 
    # Since BasicChatBot.chat is synchronous, we can run it directly, 
    # but strictly speaking for async Chainlit it's better to Wrap, 
    # however the prompt asked to "Reuse BasicChatBot" and "calls bot.chat(..)".
    # For a simple local app, calling it directly is fine, or we can use cl.make_async.
    # Given "Keep it minimal", I will call it directly. 
    
    response_text = bot.chat(message.content)
    
    await cl.Message(
        content=response_text,
    ).send()
