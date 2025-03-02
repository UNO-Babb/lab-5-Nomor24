#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter == ch:
            return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    correctLetter = word[spot]
    if letter == correctLetter:
        return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback =""
    
    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            feedback = feedback +myLetter.upper()
        elif inWord(myLetter, word) == True:
            feedback = feedback + myLetter.lower()
        else:
            feedback = feedback + "*"

    return feedback

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    guessnum = 1
    while guessnum <= 6:
        #Ask user for their guess
        validword = False
        while validword == False:
            guess = input("enter guess: ")
            guess = guess.lower()
            if guess not in wordList:
                print("Word not in list.")
                validword = False
            else:
                validword = True
        feedback = rateGuess(guess, todayWord)
        print(feedback)
        if feedback == todayWord.upper():
            print("You got it in", guessnum, "tries!")
            break
        
        guessnum = guessnum + 1

    print("The word was", todayWord)
    print("Bye")

        #Give feedback using on their word:




if __name__ == '__main__':
  main()
