from ketchup_domain.sentences import Sentences
from random import randrange

class Motivator:
    def __init__(self):
        self._sentences = Sentences()

    def _analyse(self, user_input: str) -> float:
        pass

    def _select_answer(self, sentiment_score: float) -> str:
        idx = randrange(0, self._sentences.get_number())
        return self._sentences.get_item(idx)

    def answer(self, user_input: str) -> str:
        return self._select_answer(.0)
