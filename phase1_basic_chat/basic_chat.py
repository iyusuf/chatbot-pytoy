import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def basic_chat():
    messages = [
        {"role": "system", "content": "You are a lawyer and you only answer law related topics. If asked anythong other than law then you say 'i DONT KNOW'."},
        {"role": "user", "content": "Explain law of gravity"},
    ]

    resp = client.responses.create(
        model="gpt-5.1",
        input=messages,
    )


    print(resp.output[0].content[0].text)

if __name__ == "__main__":
    basic_chat()