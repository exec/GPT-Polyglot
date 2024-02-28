from openai import OpenAI

class OpenAIUtils:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.messages = []

    def chat_completion(self, prompt, role='system'):
        self.messages.append({"role": role, "content": prompt})
        completion = self.client.chat.completions.create(model="gpt-4-0125-preview", messages=self.messages)
        response = completion.choices[0].message.content.strip()
        self.messages.append({"role": "assistant", "content": response})
        return response