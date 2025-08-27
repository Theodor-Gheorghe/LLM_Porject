# Smart Librarian - Chatbot AI pentru recomandari de carti

## Scopul proiectului

Acest proiect implementeaza un chatbot AI care recomanda carti pe baza intereselor exprimate in limbaj natural. Se utilizeaza GPT (prin OpenAI API), vector store ChromaDB pentru cautare semantica (RAG), function calling pentru obtinerea rezumatelor detaliate si functionalitati suplimentare precum input vocal, TTS si filtrare de limbaj.

---

## Structura proiectului

smart_librarian/
├── app.py                     # Launcher cu meniu CLI
├── requirements.txt           # Lista pachetelor necesare
├── README.md                  # Documentatia proiectului
├── .env.example               # Exemplu de fisier pentru cheia OpenAI
├── data/
│   ├── book_summaries.txt     # Rezumate scurte (pentru vectori)
│   └── banned_words.txt       # Cuvinte interzise (filtru limbaj)
├── embeddings/                # Folder creat automat de ChromaDB
├── src/
│   ├── chat.py                # Chatbotul principal
│   ├── retriever.py           # Vectorizare si cautare semantica
│   ├── tools.py               # Functia `get_summary_by_title` + tool GPT
│   └── utils.py               # Voice input, TTS, filtrare limbaj

---

## Instructiuni de rulare

1. Instaleaza dependentele:
pip install -r requirements.txt

2. Creeaza fisierul `.env` si adauga cheia ta OpenAI: 
OPENAI_API_KEY=sk-...    sau din .env

3. Populeaza baza ChromaDB (o singura data):
python src/retriever.py

4. Ruleaza aplicatia:
python app.py