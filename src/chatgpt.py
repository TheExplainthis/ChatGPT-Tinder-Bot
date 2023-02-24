from src.models import ModelInterface


class ChatGPT:
    def __init__(self, model: ModelInterface):
        self.model = model

    def get_response(self, text: str) -> str:
        prompt = text
        response = self.model.text_completion(f'{prompt} <|endoftext|>')
        return response


class DALLE:
    def __init__(self, model: ModelInterface):
        self.model = model

    def generate(self, text: str) -> str:
        return self.model.image_generation(text)
