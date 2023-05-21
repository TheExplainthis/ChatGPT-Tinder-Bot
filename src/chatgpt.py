import os
from src.models import ModelInterface


class ChatGPT:
    def __init__(self, model: ModelInterface):
        self.model = model

    def get_response(self, text: str) -> str:
        messages = [{
            'role': 'system', 'content': os.getenv('SYSTEM_MESSAGE')
        }, {
            'role': 'user', 'content': text
        }]
        response = self.model.chat_completion(messages)
        content = response['choices'][0]['message']['content']
        return content


class DALLE:
    def __init__(self, model: ModelInterface):
        self.model = model

    def generate(self, text: str) -> str:
        return self.model.image_generation(text)
