# Smart Librarian - Chatbot AI pentru recomandari de carti

## Scopul proiectului

Acest proiect implementeaza un chatbot AI care recomanda carti pe baza intereselor exprimate in limbaj natural. Se utilizeaza GPT (prin OpenAI API), vector store ChromaDB pentru cautare semantica (RAG), function calling pentru obtinerea rezumatelor detaliate si functionalitati suplimentare precum input vocal, TTS si filtrare de limbaj.

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


Nota: din motive legate de accesul la OpenAI embeddings, generarea vectorilor ChromaDB poate esua in unele contexte.
Pentru testare completa a functionalitatii RAG se poate folosi modelul `text-embedding-ada-002` sau un fallback manual.
Toate celelalte componente functioneaza local: GPT, rezumate, text-to-speech, speech-to-text si tool calling.
