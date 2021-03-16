import speech_recognition as sr


class Listener:
    def __init__(self):
        self.mic = sr.Microphone()
        self.rec = sr.Recognizer()

    def prep(self):
        self.rec.adjust_for_ambient_noise(self.mic)

    def listen(self) -> str:
        with self.mic as mic:
            audio = self.rec.listen(mic, )
            try:
                # Possibility to run "show_all=True" for possible alternatives
                t_audio = self.rec.recognize_google(audio, language='en')
                print(t_audio)
            except sr.UnknownValueError:
                t_audio = ""  # This is noise
            except sr.RequestError:
                # Internet is down or it failed. What to do?
                pass

            return t_audio
