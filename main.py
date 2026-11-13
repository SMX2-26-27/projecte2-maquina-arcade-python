
from jocs import janken, nana


def mostrar_menu():
    print("\n" + "=" * 35)
    print("      BENVINGUT/DA AL MINI ARCADE")
    print("=" * 35)
    print("1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("S. Sortir")
    print("=" * 35)


def main():

    while True:

        mostrar_menu()

        opcio = input("Selecciona una opció: ").strip().upper()

        if opcio == "1":
            janken()

        elif opcio == "2":
            nana()

        elif opcio == "S":
            print("\nGràcies per jugar! Fins aviat!")
            break

        else:
            print("\nOpció incorrecta. Torna-ho a intentar.")


if __name__ == "__main__":
    main()
