import pyttsx3


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        v_list = [v.id for v in voices]
        # 'default', 'english', 'en-scottish', 'english-north', 'english_rp', 'english_wmids', 'english-us', 'en-westindies'
        self.engine.setProperty('voice', voices[10].id)

    def say(self, out: str) -> None:
        self.engine.say(out)
        self.engine.runAndWait()
