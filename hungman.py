import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives >0:
        print('You have', lives, 'lives left', 'You have used these letters: ',' '.join(used_letters))
       
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        usser_letter = input('Guess a letter...').upper()
        if usser_letter in alphabet - used_letters:
            used_letters.add(usser_letter)
            if usser_letter in word_letters:
                word_letters.remove(usser_letter)
            else: 
                lives = lives -1 
                print('Letters not in word.')
        elif usser_letter in used_letters:
            print('You have guessed already that letter!')
        else:
            print('You didnt type in valid character! Try again!')
    if lives == 0:
        print('You died sorry! The word was:', word, '!')
    else:
        print('You have guessed the word:', word, 'Well done!')

usser_input = input('Your name?')
print('Hi', usser_input ,'!', 'Try to guess secret word... Good luck!') 

hangman()