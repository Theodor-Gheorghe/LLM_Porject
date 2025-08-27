from typing import Optional
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

# Dictionarul cu rezumate detaliate
book_summaries_dict = {
    "1984": (
        "Romanul lui George Orwell descrie o societate distopică dominată de Big Brother. "
        "Oamenii sunt supravegheați constant, iar gândirea liberă este considerată crimă. "
        "Winston Smith încearcă să reziste acestui regim opresiv. "
        "Este o poveste despre libertate, adevăr și manipulare ideologică."
    ),
    "The Hobbit": (
        "Bilbo Baggins, un hobbit confortabil și fără aventuri, este luat prin surprindere "
        "atunci când este invitat într-o misiune de a recupera comoara piticilor păzită de dragonul Smaug. "
        "Pe parcursul călătoriei, el descoperă curajul și resursele interioare pe care nu știa că le are. "
        "Povestea este plină de creaturi fantastice, prietenii neașteptate și momente tensionate."
    ),
    "To Kill a Mockingbird": (
        "Povestea unei fetițe care crește într-un oraș din sudul Americii anilor 1930. "
        "Tatăl ei, avocat, apără un bărbat de culoare acuzat pe nedrept. "
        "Romanul explorează teme precum rasismul, dreptatea și maturizarea."
    ),
    "Harry Potter and the Sorcerer's Stone": (
        "Harry descoperă că este vrăjitor și este invitat la Hogwarts, o școală de magie. "
        "Împreună cu prietenii lui, Harry învață despre prietenie, curaj și confruntarea cu răul. "
        "Este o poveste despre descoperirea propriei identități și lupta pentru bine."
    ),
    "The Great Gatsby": (
        "Jay Gatsby, un milionar misterios, încearcă să-și recucerească iubirea pierdută. "
        "Romanul explorează iluziile visului american, decadența și superficialitatea anilor '20."
    ),
    "Brave New World": (
        "O societate viitoare în care fericirea este obținută prin control genetic, droguri și conformism. "
        "Personajele încep să își pună întrebări despre sensul vieții. "
        "Romanul abordează teme legate de libertate, știință și manipulare socială."
    ),
    "Lord of the Flies": (
        "Un grup de copii naufragiază pe o insulă pustie și își creează propria societate. "
        "Fără reguli și autoritate, ordinea se destramă și apare violența. "
        "Romanul explorează natura umană, civilizația și haosul."
    ),
    "Animal Farm": (
        "O alegorie politică în care animalele preiau conducerea fermei. "
        "Inițial, idealurile sunt nobile, dar în timp puterea corupe. "
        "Este o critică la adresa dictaturii și a manipulării ideologice."
    ),
    "The Little Prince": (
        "Un pilot se prăbușește în deșert și întâlnește un mic prinț de pe o altă planetă. "
        "Povestea este o reflecție poetică despre iubire, prietenie și sensul vieții. "
        "Un roman simbolic despre copilărie, curiozitate și inocență."
    ),
    "The Catcher in the Rye": (
        "Holden Caulfield, un adolescent confuz, fuge de la școală și rătăcește prin New York. "
        "Povestea reflectă lupta cu identitatea, singurătatea și maturizarea. "
        "Este un portret sincer al anxietăților adolescenței."
    )
}

# Modelul de validare (pentru OpenAI function calling)
class SummaryInput(BaseModel):
    title: str

# Functia care returneaza rezumatul
def get_summary_by_title(title: str) -> str:
    title = title.strip().lower()
    for key in book_summaries_dict:
        if key.strip().lower() == title:
            return book_summaries_dict[key]
    return "Nu există un rezumat disponibil pentru titlul solicitat."


# Tool-ul definit pentru GPT
openai_tool = {
    "type": "function",
    "function": {
        "name": "get_summary_by_title",
        "description": "Returneaza rezumatul complet al unei carti dupa titlul exact.",
        "parameters": SummaryInput.model_json_schema()
    }
}

# Testare rapida

#if __name__ == "__main__":
#    print(get_summary_by_title("1984"))
