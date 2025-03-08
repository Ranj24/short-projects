import random
import re
from nltk.corpus import words
word_list = words.words()


word = random.choice(word_list)
guesses = "_"*len(word)
print(guesses)
lives = 10
print("You have "+str(lives)+" lives! Good Luck!")
tried = set()

while "_" in guesses and lives !=0:
    guess = input("Guess a letter: \n")

    if guess in word and len(guess)==1:
        positions = [match.start() for match in re.finditer(guess, word)]
        for pos in positions:
            guess_list = list(guesses)
            guess_list[pos] = guess
            guesses = "".join(guess_list)
        print(guesses)
    else:
        if guess in tried:


            print("You have already guessed that letter!")
        if guess not in tried:
            print("Wrong")
            lives -= 1
            tried.add(guess)

        print(str(lives) + " lives left!")
if lives == 0:
    print("Game over")
    print(word)
if "_" not in guesses:
    print("You win")
