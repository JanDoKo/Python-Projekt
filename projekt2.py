"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Dolejší
email: j-dolejsi@koito-czech.cz
discord: Jan D#4030
"""

import os
from random import randint

# lenght je délka odhadnovaného čísla tato hodnota se může pohybovat v rozmezí 1 - 10
lenght = 4
separator = '─' * 63


def greetings() -> None:
    '''
    Popis:
    -----
    Funkce vytvoří jednoduchý pozdrav, oddělený separatorem
    Argumenty se oddělí pomocí separátoru.
    '''
    print("Hi there!", 
        separator, 
        f"I've generated a random {lenght} digit number for you.",
        "Let's play a bulls and cows game.", 
        separator,
        sep='\n')


def set_number() -> int:
    '''
    Popis:
    -----
    Funkce vytvoří číslo od 1000 do 9999 
    (v případě změny lenght hodnoty jiné délky) 
    '''
    number = str(randint(int((10**lenght/10)),int('9'*lenght)))
    while len(set(number)) != lenght:
        number = str(randint(int((10**lenght/10)),int('9'*lenght)))
    return(number)


def guess_comparison(number,guess) -> list:
    '''
    Popis:
    -----
    Funkce vrátí list, který bude obsahovat 2 číselné hodnoty.
    První číslo (bulls) bude obsahovat stejné hodnoty na stejném místě.
    druhé číslo (cows) pak stejné hodnoty ale na odlišných místech.

    Ukázka:
    -----
    numbers: str = '6834'
    guess: str = '1234'
    Funkce vrátí hodnotu: list = [2,0]
    -----
    numbers: str = '8154'
    guess: str = '1234'
    Funkce vrátí hodnotu: list = [1,1]   
    '''
    bulls = 0
    cows = 0
    for i in range(len(number)):
        if guess[i] == number[i]:
            bulls += 1
            cows -= 1
        if guess[i] in number:
            cows += 1
    return [bulls, cows]


def plurality_bulls(count) -> str:
    '''
    Popis:
    -----
    Funkce na základě zadané hodnoty vrátí hodnotu bull nebo bulls.

    Ukázka:
    -----
    count: int = 1
    Funkce vrátí hodnotu: str = 'bull'
    -----
    count: int = 3
    Funkce vrátí hodnotu: str = 'bulls'
    '''
    if count == 1:
        return 'bull'
    else:
        return 'bulls'


def plurality_cows(count) -> str:
    '''
    Popis:
    -----
    Funkce na základě zadané hodnoty vrátí hodnotu bull nebo bulls.

    Ukázka:
    -----
    count: int = 1
    Funkce vrátí hodnotu: str = 'cow'
    -----
    count: int = 0
    Funkce vrátí hodnotu: str = 'cows'   
    '''
    if count == 1:
        return 'cow'
    else:
        return 'cows'


def evaluation(gset) -> None:
    '''
    Popis:
    -----
    Funkce slouží pro výpis tabulky s přehledem hádaných čísel. 
    gset bude obsahovat list hádaných listů s hodnotami 
    [číslo pokusu, hádané číslo, vyhodnocení],
    každý tento list se pak vypíše na svůj řádek tabulky.
    '''
    column1 = 7
    column2 = 12
    column3 = 38
    greetings()
    print("┌",(column1+1)*"─","┬",(column2)*"─","┬",(column3+1)*"─","","┐",sep="")
    print("│ ","Guess".center(column1),"│","Your tip".center(column2),"│","Result".center(column3)," │",sep="") 
    print("├",(column1+1)*"─","┼",(column2)*"─","┼",(column3+1)*"─","","┤",sep="")
    for x in gset:
       print("│",str(x[0]).rjust(column1)," │ ",str(x[1]).rjust(column2-2)," │ ",str(x[2]).ljust(column3),"│",sep="")
    print("└",(column1+1)*"─","┴",(column2)*"─","┴",(column3+1)*"─","","┘",sep="")


def final_evaluation(guess) -> None:
    '''
    Popis:
    -----
    Jednoduchá funkce pro výpis ohodnocení počtu pokusů.

    Ukázka:
    -----
    count: int = lenght (standatně 4)
    Funkce vrátí hodnotu: str = "That's amazing!"
    -----
    count: int > 3*lenght (standatně 12)
    Funkce vrátí hodnotu: str = "That's not so good!"  
    '''
    if guess < lenght:
        print("That's amazing!")
    elif guess < 3*lenght:
        print("That's average!")
    else:
        print("That's not so good!")


def game() -> None:
    '''
    Popis:
    -----
    Hlavní funkce, která po uvítání vyhodnotí hádané číslo
    - vyhodnotí, zda číslo neobsahuje nečíselné znaky
    - zda číslo má správnou délku (definovanou lenght, standartně 4 znaky)
    - zda se v hádaném čísle neopakují stejné číslice
    - zda číslo nezačíná 0

    Pokud číslo splňuje požadované podmínky, funkce vyhodnotí odhad 
    a za pomoci dalších propojených funkcí poskytne výpis a vyhodnocení.

    Hru lze kdykoliv ukončit zadáním hodnoty 'quit'

    '''
    os.system('cls')
### Program pozdraví užitele a vypíše úvodní text (pro přehlednost ponechaný komentář)
    greetings()
    guess_count = 0
    guessset = []
### Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0) (pro přehlednost ponechaný komentář)
    number = set_number()
    while True:
### Hráč hádá číslo. (pro přehlednost ponechaný komentář)
        guesslist = []
        print("Enter a number: ", separator, sep='\n')
#        print(number)
        guess = input('>>> ')
        guesslist.append(guess)
        if guess == 'quit':
            print('The game was terminated by the user. Thank you for playing.')
            break
### Program jej upozorní, pokud bude obsahovat nečíselné znaky (pro přehlednost ponechaný komentář)
        elif not(guess.isnumeric()):
            guesslist.append('Your choice is not number!')
            guesslist.insert(0,'-')
            os.system('cls')
### Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla (délku čísla (pozn.)) (pro přehlednost ponechaný komentář)
        elif len(guess) != lenght:
            guesslist.append('The lenght is invalid!')
            guesslist.insert(0,'-')
            os.system('cls')
### Program jej upozorní, pokud bude obsahovat duplicity (pro přehlednost ponechaný komentář)
        elif len(set(guess)) != lenght:
            guesslist.append('In your guess are not unique numbers!')
            guesslist.insert(0,'-')
            os.system('cls')
### Program jej upozorní, pokud začínat nulou (pro přehlednost ponechaný komentář)
        elif guess[0] == '0':
            guesslist.append('Your choice cannot start with 0!')
            guesslist.insert(0,'-')
            os.system('cls')
### Program vyhodnotí tip uživatele (pro přehlednost ponechaný komentář)
        else:
            guess_comparison(number,guess)
            guess_count += 1
            guesslist.insert(0,guess_count)
### Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows). (pro přehlednost ponechaný komentář)
            guesslist.append(f'{guess_comparison(number,guess)[0]} {plurality_bulls(guess_comparison(number,guess)[0])}, {guess_comparison(number,guess)[1]} {plurality_cows(guess_comparison(number,guess)[1])}')
            os.system('cls')
            if guess_comparison(number,guess)[0] == lenght:
                guessset.append(guesslist)
                evaluation(guessset)
                print(f"Correct, you've guessed the right number in {guess_count} guesses!")
                final_evaluation(guess_count)
                x = input("Press enter to quit.")
                break  
        guessset.append(guesslist)
        evaluation(guessset)


if __name__ == '__main__':
    game()