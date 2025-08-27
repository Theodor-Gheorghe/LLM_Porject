import pyttsx3
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from src.retriever import semantic_search
from src.tools import get_summary_by_title, openai_tool, book_summaries_dict
from src.utils import contine_limbaj_nepotrivit, asculta_microfon

# Încarcă cheia din .env
load_dotenv()
client = OpenAI()

# Inițializare motor text-to-speech
engine = pyttsx3.init()

def spune(text):
    engine.say(text)
    engine.runAndWait()

def chat():
    print("Întreabă-mă despre ce fel de carte cauți.")
    print("Tastează 'exit' pentru a închide conversația.")

    # Alegere Voice Mode
    voice_mode = input("Activezi Voice Mode? (da/nu): ").strip().lower() in ["da", "d", "y", "yes"]

    while True:
        # Obține input de la utilizator (voce sau tastatură)
        if voice_mode:
            user_input = asculta_microfon()
        else:
            user_input = input("\nTu: ")

        # Iesire
        if user_input.lower() in ["exit", "quit"]:
            print("La revedere!")
            break

        # Verificare limbaj nepotrivit
        if contine_limbaj_nepotrivit(user_input):
            print("Smart Librarian: Îți recomand să folosești un limbaj adecvat.")
            continue

        # Căutare semantică reală
        results = semantic_search(user_input)
        if not results["metadatas"][0]:
            print("Nu am găsit nicio carte potrivită.")
            continue

        top_result = results["metadatas"][0][0]
        title = top_result["title"]

        print(f"[DEBUG] Titlu returnat de Chroma: {title}")

        # Cerere către GPT + Tool integration
        response = client.chat.completions.create(
            model="gpt-4o",
            tools=[openai_tool],
            tool_choice="auto",
            messages=[
                {
                    "role": "system",
                    "content": "Ești un bibliotecar AI care recomandă cărți pe baza intereselor utilizatorului. "
                               "După ce recomanzi o carte, dacă este cazul, apelează tool-ul get_summary_by_title pentru a arăta rezumatul complet."
                },
                {
                    "role": "user",
                    "content": f"Întrebarea: {user_input}\nRecomandă cartea: {title}, explicând de ce se potrivește."
                }
            ]
        )

        message = response.choices[0].message

        # Afișare răspuns conversațional fallback dacă content e None
        if message.content:
            print(f"\nSmart Librarian:\n{message.content}")
            spune(message.content)
        else:
            print("\nSmart Librarian: Am generat un răspuns, dar fără text explicit (doar function call).")

        # Verificare apelare tool pentru rezumat
        if message.tool_calls:
            for tool_call in message.tool_calls:
                if tool_call.function.name == "get_summary_by_title":
                    args = json.loads(tool_call.function.arguments)
                    summary = get_summary_by_title(args["title"])
                    print("\nRezumat detaliat:")
                    print(summary)
                    spune(summary)

if __name__ == "__main__":
    chat()
