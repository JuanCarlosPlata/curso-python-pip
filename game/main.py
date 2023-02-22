from time import sleep
import sys
from os import system, name
import random


# Funcion para validar si son numeros lo que se ingresa.


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def validar_numero(text, text2):
    while True:
        try:
            delay_print(text)
            valor = int(input("\n=> "))
        except ValueError:
            delay_print(f"Invalid option\nPlease only enter numbers{text2}\n")
            sleep(1.5)
            clear()
            title()
            continue
        return valor
# Funcion para escribir letra por letra


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.02)  # Tiempo de espera estre cada letra


def resultado_del_juego(resultado):
    sleep(0.5)
    delay_print(
        f"You chose {options[user_option]} Computer chose {options[computer_option]}\n{resultado}\n")
    sleep(2)


def volver_a_jugar(text):
    while True:
        repetir = validar_numero(f"\nPlay again?\n1-Yes  2-No", text)
        if repetir == 2:
            delay_print("Thanks for playing, see you next time!")
            global ciclo
            ciclo = 0
            return ciclo
        elif repetir == 1:
            return clear()
        else:
            delay_print(f"Invalid option\nPlease only enter numbers{text}\n")
            sleep(1.5)
            clear()
            title()


def title():
    print("______           _     ______                             _____      _                         ")
    print("| ___ \         | |    | ___ \                           /  ___|    (_)                        ")
    print("| |_/ /___   ___| | __ | |_/ /_ _ _ __  _ __   ___ _ __  \ `--.  ___ _ ___ ___  ___  _ __ ___  ")
    print("|    // _ \ / __| |/ / |  __/ _` | '_ \| '_ \ / _ \ '__|  `--. \/ __| / __/ __|/ _ \| '__/ __| ")
    print("| |\ \ (_) | (__|   <  | | | (_| | |_) | |_) |  __/ |    /\__/ / (__| \__ \__ \ (_) | |  \__ \ ")
    print("\_| \_\___/ \___|_|\_\ \_|  \__,_| .__/| .__/ \___|_|    \____/ \___|_|___/___/\___/|_|  |___/ ")
    print(f"                                 | |   | |           Round {round}                                     ")
    print(
        f"                                 |_|   |_|      you {score[0]} Computer {score[1]}            ")



def run():
    global user_option, computer_option, score, options, ciclo, round
    score = [0, 0]
    round = 1
    options = ("", "Rock \U0001f44a", "Paper \u270B", "Scissor\u2702\ufe0f ")
    #          0      1                  2                3
    ciclo = 1
    while ciclo == 1:
        clear()
        title()
        user_option = validar_numero(
            "Enter a choice\n1 Rock\U0001f44a\n2 Paper\u270B\n3 Scissor\u2702\ufe0f \n4 Exit.", " between 1 and 4.")
        if user_option not in (1, 2, 3, 4):
            delay_print(
                "Invalid option\nPlease only enter numbers between 1 and 4\n")
            sleep(1.5)
            continue
        if user_option == 4:
            sleep(0.5)
            ciclo = 0
            delay_print("Thanks for playing, see you next time!")
            sleep(1)
            clear()
        computer_option = random.randint(1, 3)
        if user_option == computer_option:
            resultado_del_juego("It's a tie!")
            volver_a_jugar(" between 1 and 2.")
        elif user_option == 1 and computer_option == 2 or user_option == 2 and computer_option == 3 or user_option == 3 and computer_option == 1:
            resultado_del_juego("You lose")
            score[1] += 1
            volver_a_jugar(" between 1 and 2.")
        elif user_option == 1 and computer_option == 3 or user_option == 2 and computer_option == 1 or user_option == 3 and computer_option == 2:
            resultado_del_juego("You win!")
            score[0] += 1
            volver_a_jugar(" between 1 and 2.")
        round +=1

if __name__ == "__main__":
    run()