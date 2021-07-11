import os
import random
from functools import reduce


def logo_hangman():
    print('''

    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
''')


def image_hangman(death):
    die0 = '''













'''
    die1 = '''







        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die11 = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  @    
        __║__________      └─┼─┘
      /   ║         /|       │
     /____________ / |      / '''+chr(92)+'''
    |             | /      d   b
    |_____________|/

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10, 11: die11}
    print(deaths.get(death))


def compare_letter(letter, dict_word, discovered, fail):
    for l in range(len(dict_word)):
        if dict_word.get(l) == letter:
            discovered[l] = letter + ' '
            fail = False
    return discovered, fail


def read_word():
    word_li = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data_words:
        word = random.choice([word.strip().upper() for word in data_words])
    for letter in word:
        if letter == 'Á':
            letter = 'A'
        elif letter == 'É':
            letter = 'E'
        elif letter == 'Í':
            letter = 'I'
        elif letter == 'Ó':
            letter = 'O'
        elif letter == 'Ú':
            letter = 'U'
        word_li.append(letter)
    return ''.join(word_li)


def run():
    word = read_word()
    dict_word = {i[0] : i[1] for i in enumerate(word)}
    discovered = ['- ' for i in range (len(dict_word))]
    deaths = 0
    while True:
        os.system('clear')
        logo_hangman()
        image_hangman(deaths)
        letter = input('''¡Adivina la palabra!
'''+ ''.join(discovered) +'''
Ingresa una letra: ''').upper()
        fail = True
        discovered,fail = compare_letter(letter, dict_word, discovered, fail)
        if fail == True:
            deaths += 1
            if deaths == 10:
                os.system('clear')
                logo_hangman()
                image_hangman(deaths)
                print('¡Perdiste! La palabra era ' + word)
                deaths = 0
                again = input('¿Quieres intetnarlo otra vez? (1-Si 0-No):  ')
                if again == '1':
                    word = read_word()
                    dict_word = {i[0] : i[1] for i in enumerate(word)}
                    discovered = ['- ' for i in range (len(dict_word))]
                    continue
                else:
                    print('Gracias por jugar :)')
                    break
        if ''.join(discovered).replace(' ','') == word:
            os.system('clear')
            logo_hangman()
            image_hangman(11)
            print('Tuviste ', deaths, ' erorres')
            deaths = 0
            again = input('¿Quieres intetnarlo otra vez? (1-Si 0-No):  ')
            if again == '1':
                word = read_word()
                dict_word = {i[0] : i[1] for i in enumerate(word)}
                discovered = ['- ' for i in range (len(dict_word))]
                continue
            else:
                print('Gracias por jugar :)')
                break


if __name__ == '__main__':
    os.system('clear')
    run()