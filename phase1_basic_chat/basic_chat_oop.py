import os
from dotenv import load_dotenv
from openai import OpenAI


class BasicChatBot:
    """
    A simple law-focused chatbot using the OpenAI Responses API.
    """

    def __init__(
        self,
        model: str = "gpt-4.1",
        system_prompt: str | None = None,
    ) -> None:
        load_dotenv()
        self.client = OpenAI()
        self.model = model
        self.system_prompt = (
            system_prompt
            or "You are a lawyer and you only answer law related topics. "
            "If asked anythong other than law then you say 'i DONT KNOW'."
        )

    def chat(self, user_message: str) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message},
        ]

        resp = self.client.responses.create(
            model=self.model,
            input=messages,
        )

        return resp.output[0].content[0].text


def main() -> None:
    bot = BasicChatBot()
    answer = bot.chat("Explain law of gravity")
    print(answer)


if __name__ == "__main__":
    main()

