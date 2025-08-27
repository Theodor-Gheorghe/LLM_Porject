import os
import speech_recognition as sr

def contine_limbaj_nepotrivit(text: str) -> bool:
    path = "data/banned_words.txt"
    if not os.path.exists(path):
        return False

    with open(path, "r", encoding="utf-8") as f:
        cuvinte = [linie.strip().lower() for linie in f if linie.strip()]

    text = text.lower()
    return any(cuvant in text for cuvant in cuvinte)

def asculta_microfon() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ascult... vorbeste acum.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ro-RO")
        print(f"Am inteles: {text}")
        return text
    except sr.UnknownValueError:
        print("Nu am inteles ce ai spus.")
        return ""
    except sr.RequestError as e:
        print(f"Eroare la recunoastere: {e}")
        return ""
