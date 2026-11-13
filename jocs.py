from robot import robot
import random
from robot import robot

def janken():

    # Crear una instancia del robot
    machine = robot()

    print("\n" + "=" * 35)
    print("       PEDRA, PAPER, TISORA")
    print("=" * 35)

    # Seleccionar la modalitat
    print("\nSelecciona la modalitat:")
    print("1. El primer que arribi a 3 victories")
    print("2. Millor de 5 rondes")

    while True:
        mode = input("\nEscull una opcio (1/2): ")

        if mode == "1":
            max_victories = 3
            max_rondes = None
            break

        elif mode == "2":
            max_victories = None
            max_rondes = 5
            break

        else:
            print("Opcio incorrecta. Torna-ho a intentar.")

    # Inicialitzar puntuacions
    victories_jugador = 0
    victories_robot = 0
    ronda = 0

    # Bucle de les partides
    while True:

        ronda += 1

        print(f"\n--- RONDA {ronda} ---")

        # Demanar jugada a l'usuari
        while True:
            jugador = input(
                "Escull pedra, paper o tisora: "
            ).lower().strip()

            if jugador in ["pedra", "paper", "tisora"]:
                break

            print("Jugada incorrecta. Torna-ho a intentar.")

        # Obtenir jugada del robot
        jugada_robot = machine.playing()

        print(f"\nTu has escollit: {jugador}")
        print(f"{machine.name} ha escollit: {jugada_robot}")

        # Comparar les jugades
        if jugador == jugada_robot:
            print("Empat!")

        elif (
            (jugador == "pedra" and jugada_robot == "tisora")
            or (jugador == "paper" and jugada_robot == "pedra")
            or (jugador == "tisora" and jugada_robot == "paper")
        ):
            print("Has guanyat aquesta ronda!")
            victories_jugador += 1

        else:
            print("El robot guanya aquesta ronda!")
            victories_robot += 1

        # Mostrar puntuacions
        print("\nPUNTUACIO:")
        print(f"Jugador: {victories_jugador}")
        print(f"Robot: {victories_robot}")

        # Comprovar si s'ha arribat al final
        if max_victories is not None:

            if victories_jugador == max_victories:
                break

            elif victories_robot == max_victories:
                break

        elif ronda == max_rondes:
            break

    # Resultat final
    print("\n" + "=" * 35)
    print("          RESULTAT FINAL")
    print("=" * 35)

    if victories_jugador > victories_robot:
        print("Has guanyat la partida!")

    elif victories_robot > victories_jugador:
        print("El robot guanya la partida...")

    else:
        print("La partida ha acabat en empat!")

    print(f"\nResultat: {victories_jugador} - {victories_robot}")
    print("=" * 35)



def nana():

    print("\n" + "=" * 35)
    print("        ENDEVINAR EL NUMERO")
    print("=" * 35)

    # Generar un numero aleatori entre 1 i 100
    numero_secret = random.randint(1, 100)

    # Inicialitzar el comptador d'intents
    intents = 0

    print("\nHe pensat un numero entre 1 i 100.")
    print("Intenta endevinar-lo!")

    # Bucle principal del joc
    while True:

        try:
            numero = int(input("\nIntrodueix un numero: "))
            intents += 1

            if numero < 1 or numero > 100:
                print("El numero ha d'estar entre 1 i 100.")

            elif numero < numero_secret:
                print("Massa baix! Torna-ho a intentar.")

            elif numero > numero_secret:
                print("Massa alt! Torna-ho a intentar.")

            else:
                print("\nENHORABONA! Has encertat!")
                print(f"El numero secret era {numero_secret}.")
                print(f"Ho has aconseguit en {intents} intents!")
                break

        except ValueError:
            print("Error: has d'introduir un numero enter.")
