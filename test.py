import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    voices = engine.getProperty('voices')
    # Setting voice according to the language - Assuming index 1 for Urdu, change as needed
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

# Example usage:
text_to_speak = "میرا نام ہے ۔"
speak(text_to_speak)
