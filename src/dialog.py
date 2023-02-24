
class Dialog:
    PREFIX = """
        You are now playing the role of [Sender] and your task is to respond to [Receiver] in the conversation below. Your response should not exceed 50 words and end with a question. Please respond in the language used by [Sender].
    """

    def generate_input(self, from_user_id, to_user_id, dialog):
        context = '\n'.join([str(d).replace(from_user_id, '[Sender]').replace(to_user_id, '[Receiver]') for d in dialog])
        return f'{self.PREFIX} \n\n{context}\n[Sender]:'
