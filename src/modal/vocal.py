import speech_recognition as sr

class Vocal:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self) -> str:
        with self.microphone as source:
            print("Ecoute de la commande...")
            audio = self.recognizer.listen(source)

        try:
            print("G konpri: " + self.recognizer.recognize_google(audio, language="fr-FR"))
            return self.recognizer.recognize_google(audio, language="en-EN")
        except sr.UnknownValueError:
            print("G ri un konpri")
        except sr.RequestError as e:
            print("G buggé. Erreur : ".format(e))

    def interpret(self, text) -> int:
        if "School" in text:
            return (1,26)
        if "Library" in text:
            return 4
        if "Cinema" in text:
            return 7
        if "Bus" or "Station" in text:
            return (18,34)
        if "Mall" in text:
            return 28
        if "Post" or "Office" in text:
            return 30
        if "Home" in text:
            return 38
        else:
            return -1
        