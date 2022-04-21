import random

HANGMAN = ['''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


def getWord():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        return random.choice(words) 

 
def displayBoard(HANGMAN, wrongLetter, rightLetter, secretWord):
    print(HANGMAN[len(wrongLetter)])
    print ("")
    end = " "
    print ('Wrong letters:', end)
    for letter in wrongLetter:
        print (letter, end)
    print ("")
    space = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in rightLetter:
            space = space[:i] + secretWord[i] + space[i+1:]
    for letter in space: 
        print (letter, end)
    print ("")
 
def pickLetter(someLetter):
    while True:
        print ('Guess a letter:')
        letter = input()
        letter = letter.lower()
        if len(letter) != 1:
            print ('Write one letter at a time.') 
        elif letter in someLetter:
            print ('You have already picked this letter')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Pick a letter.')
        else:
            return letter
 
def playAgain():
    print ('Want to play again? (y for Yes, n for No)')
    return input().lower().startswith('y')
 
print ('H A N G M A N')
wrongLetter = ""
rightLetter = ""

secretWord = getWord()
endGame = False
while True:
    displayBoard(HANGMAN, wrongLetter, rightLetter, secretWord)
    letter = pickLetter(wrongLetter + rightLetter)
    if letter in secretWord:
        rightLetter = rightLetter + letter
        foundLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in rightLetter:
                foundLetters = False
                break
        if foundLetters:
            print ('Good job! the secret word is: "' + secretWord + '"! You have won!')
            endGame = True
    else:
        wrongLetter = wrongLetter + letter
        if len(wrongLetter) == len(HANGMAN) - 1:
            displayBoard(HANGMAN, wrongLetter, rightLetter, secretWord)
            print ('You are out of letters\nAfter ' + str(len(wrongLetter)) + ' wronged letters and ' + str(len(rightLetter)) + ' right letters, the word was "' + secretWord + '"')
            endGame = True
    if endGame:
        if playAgain():
            wrongLetter = ""
            rightLetter = ""
            endGame = False
            secretWord = getWord()
        else:
            break
