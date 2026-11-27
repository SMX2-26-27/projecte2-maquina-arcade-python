# Mini Arcade en Python

Aplicació de consola escrita en Python que ofereix dos jocs simples: **Pedra, Paper, Tisora** i **Endevinar el Número**. Els jocs es poden executar repetidament des d'un menú principal fins que l'usuari decideix sortir.

## Requisits

- Python 3
- No cal instal·lar cap dependència externa

## Executar l'aplicació

Des del directori del projecte:

```bash
python3 main.py
```

## Funcionament general

En iniciar el programa es mostra un menú amb aquestes opcions:

- `1`: iniciar Pedra, Paper, Tisora.
- `2`: iniciar Endevinar el Número.
- `S`: sortir de l'aplicació.

Una opció diferent de les disponibles mostra un missatge d'error i torna a mostrar el menú.

## Estructura del projecte

```text
.
├── main.py    # Punt d'entrada i menú principal
├── jocs.py    # Implementació dels dos jocs
├── robot.py   # Classe del robot que juga aleatòriament
└── README.md  # Documentació del projecte
```

### `main.py`

Conté la funció `mostrar_menu()`, que mostra les opcions disponibles, i la funció `main()`, que llegeix l'opció introduïda per l'usuari i crida el joc corresponent:

- `janken()` per a Pedra, Paper, Tisora.
- `nana()` per a Endevinar el Número.
- La lletra `S` finalitza el programa.

### `jocs.py`

Conté la lògica dels dos jocs:

- `janken()` implementa Pedra, Paper, Tisora.
- `nana()` implementa Endevinar el Número.

### `robot.py`

Defineix la classe `robot`, que té:

- `name`: nom del robot, amb el valor `machine`.
- `game`: llista de jugades possibles: pedra, paper i tisora.
- `playing()`: retorna una jugada aleatòria.

## Pedra, Paper, Tisora

El joc demana triar una modalitat:

1. **Primer a 3 victòries:** guanya qui aconsegueixi tres rondes abans que ho faci l'oponent.
2. **Millor de 5 rondes:** es juguen com a màxim cinc rondes i guanya qui tingui més victòries.

A cada ronda:

1. L'usuari escriu `pedra`, `paper` o `tisora`.
2. El robot escull aleatòriament una de les tres opcions.
3. El programa compara les jugades i mostra el resultat.
4. S'actualitza i mostra la puntuació.

Les regles són:

- Pedra guanya a tisora.
- Paper guanya a pedra.
- Tisora guanya a paper.
- Si les dues jugades coincideixen, la ronda acaba en empat.

Al final es mostra el resultat global i la puntuació entre jugador i robot.

## Endevinar el Número

El programa genera aleatòriament un número secret entre `1` i `100` ambdues inclosos.

Cada intent:

- Els valors fora del rang indiquen que el número ha d'estar entre 1 i 100.
- Els valors per sota del número secret indiquen que el número és massa baix.
- Els valors per sobre indiquen que el número és massa alt.
- Quan l'usuari encerta, es mostra el número secret i el nombre total d'intents.
- Si s'introdueix text que no es pot convertir a enter, el programa mostra un error i demana un altre número.

## Notes d'ús

- Les opcions i les jugades no distingeixen majúscules i minúscules.
- Les opcions del menú admeten espais inicials i finals gràcies a `strip()`.
- Les jugades del jugador també admeten majúscules i espais extres gràcies a `lower()` i `strip()`.
