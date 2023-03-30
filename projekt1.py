### 1. Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Dolejší
email: j-dolejsi@koito-czech.cz
discord: Jan D#4030
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = (43 * "─")

### 2.Vyžádá si od uživatele přihlašovací jméno a heslo
username = input("username:")
password = input("password:")

### 3. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
### Registrovaní uživatelé
### +------+-------------+
### | user |   password  |
### +------+-------------+
### | bob  |     123     |
### | ann  |   pass123   |
### | mike | password123 |
### | liz  |   pass123   |
### +------+-------------+

username_password = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

if username in username_password.keys() and username_password[username] == password:
### 4. pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
    print(separator)
    print("Welcome to the app,",username)
    print("We have 3 texts to be analyzed.")
    print(separator)
else:
### 5. pokud není registrovaný, upozorni jej a ukonči program
    print(separator)
    print("unregistered user, terminating the program.")
    print(separator)
    input("Press Enter to exit program...")
    exit()

### x5. program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
text_number = input(f"Enter a number btw. {list(range(1,len(TEXTS)+1))[0]} and {list(range(1,len(TEXTS)+1))[-1]} to select: ")

### x5a. pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
### x5b. pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
if text_number in list(str(textnr) for textnr in list(range(1,len(TEXTS)+1))):
    selected_text = TEXTS[int(text_number)-1]
    print(separator)
else:
    print(separator)
    print("Your choice is invalid!!!")
    print(separator)
    input("Press Enter to exit program...")
    exit()

### 6. pro vybraný text spočítá následující statistiky:
pure_text = []
for word in selected_text.split():
    pure_word = word.strip(".,?!")
    pure_text.append(pure_word)

### 6a. počet slov
print(f'There are {len(pure_text)} words in the selected text.')

### 6b. počet slov začínajících velkým písmenem
titlecase_count = [x.istitle() for x in pure_text]
print(f'There are {titlecase_count.count(True)} titlecase words.')

### 6c. počet slov psaných velkými písmeny
uppercase_count = [x.isupper() and x.isalpha() for x in pure_text]
print(f'There are {uppercase_count.count(True)} uppercase words.')

### 6d. počet slov psaných malými písmeny
lowercase_count = [x.islower() for x in pure_text]
print(f'There are {lowercase_count.count(True)} lowercase words.')

### 6e. počet čísel (ne cifer)
numeric_count = [x.isnumeric() for x in pure_text]
print(f'There are {numeric_count.count(True)} numeric strings.')

### 6f. sumu všech čísel (ne cifer) v textu
numeric_sum = 0
for numeric in pure_text:
    if numeric.isnumeric():
        numeric_sum = numeric_sum + int(numeric)
    else:
        numeric_sum = numeric_sum
print(f'The sum of all the numbers {numeric_sum}.')

print(separator)

### 7. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.
# Vytvoření slovníku
len_count = {}
for lword in [len(x) for x in pure_text]:
    if lword not in len_count:
        len_count[lword] = 1
    else:
        len_count[lword] = len_count[lword] + 1
sorted_len = dict(sorted(len_count.items()))

# Spočtení potřebné šířky sloupce podle velikosti hodnot (plus okraj velvo a vpravo)
column1 = (len(str(max(sorted_len.keys())))) + 2
column2 = (max(sorted_len.values())) + 2
column3 = (len(str(max(sorted_len.values())))) + 2

# Výpis grafu ze slovníku délky slov
print("┌",column1*"─","┬",column2*"─","┬",column3*"─","","┐",sep="")
print("│","LEN".center(column1),"│","OCCURENCES".center(column2),"│","NR".center(column3),"│",sep="") 
print("├",column1*"─","┼",column2*"─","┼",column3*"─","","┤",sep="")
for lword in sorted_len:
    print("│",str(lword).center(column1),"│ ",str(sorted_len[lword]*"*").ljust(column2-1),"│",str(sorted_len[lword]).center(column3),"│",sep="")
print("└",column1*"─","┴",column2*"─","┴",column3*"─","","┘",sep="")
input("Press Enter to exit program...")

### 8. Po spuštění by měl průběh vypadat následovně:
### $ python projekt1.py
### username:bob
### password:123
### ----------------------------------------
### Welcome to the app, bob
### We have 3 texts to be analyzed.
### ----------------------------------------
### Enter a number btw. 1 and 3 to select: 1
### ----------------------------------------
### There are 54 words in the selected text.
### There are 12 titlecase words.
### There are 1 uppercase words.
### There are 38 lowercase words.
### There are 3 numeric strings.
### The sum of all the numbers 8510
### ----------------------------------------
### LEN|  OCCURENCES  |NR.
### ----------------------------------------
###   1|*             |1
###   2|*********     |9
###   3|******        |6
###   4|***********   |11
###   5|************  |12
###   6|***           |3
###   7|****          |4
###   8|*****         |5
###   9|*             |1
###  10|*             |1
###  11|*             |1


### 9. pokud uživatel není registrovaný:
### $ python projekt1.py
### username:marek
### password:123
### unregistered user, terminating the program..
