class Motivator:
    def __init__(self):
        # What does the motivator do?
        # Should it decide the sentiment of a sentence?
        # How?
        # And if so, what should it store?
        # Maybe the different storage objects that it then uses
        # Should these be passed from above,
        # or created in the constructor?
        pass

    def _analyse(self, user_input: str) -> float:
        pass

    def _select_answer(self, sentiment_score: float) -> str:
        pass

    def answer(self, user_input: str) -> str:
        pass
