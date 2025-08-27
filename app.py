from src.chat import chat
from src.tools import get_summary_by_title

def afiseaza_rezumat_manual():
    titlu = input("Introdu titlul exact al cartii: ").strip()
    rezumat = get_summary_by_title(titlu)
    print(f"\nRezumatul pentru '{titlu}':\n{rezumat}")

def main():
    while True:
        print("\n==== Smart Librarian ====")
        print("1. Chat cu AI (text/voce)")
        print("2. Vizualizeaza un rezumat manual")
        print("3. Iesire")
        optiune = input("Alege o optiune: ")

        if optiune == "1":
            chat()
        elif optiune == "2":
            afiseaza_rezumat_manual()
        elif optiune == "3":
            print("La revedere!")
            break
        else:
            print("Optiune invalida. Incearca din nou.")

if __name__ == "__main__":
    main()
