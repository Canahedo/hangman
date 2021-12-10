'''
Hangman
Written by Canahedo
Python3
2021
'''

from words import wordList # Source of potential words
from random import choice # Chooses the word
from gal import low as gallow # Provides gallows images

# Takes input, rejects if not alphabetical or >1 char, or if it has already been used, returns lowercase
def guess(used):
    guess = "" # Initialize
    while not guess.isalpha(): # Loops if input is not alphabetical
        guess = input("Enter guess: ").lower() # Takes input, converts to lower
        if len(guess) != 1 or guess in used: guess = "" # Rejects >1 char input, or if already used
    return guess

# Draws gameboard with gallows at nth step, and displays guessed letters
def draw(n,wrong,board,word):
    print(f"\n------------------\n------------------\nWelcome to Hangman\nFind the hidden word\n{len(word)} letters long\nGuess a letter\n------------------")
    print(gallow[n])
    print(f"Incorrect guesses: {wrong}")
    print(f"Word: {board}")

# Adds letter to board, which are found in word
def vanna(board,letter,word):
    i, n = 0, 0 # i indexes the loop, n counts instances
    for char in word:
        if letter == char:
            n += 1
            board = board[:i] + letter + board[i+1:]
        i += 1
    print(f"Found {n}x {letter}!")
    return board

word = choice(wordList) # Randomly choose word from list
board, wrong = "", "" # Initialize main board and incorrect guess board
for letter in range(len(word)): board += "_" # Add a space to board for each letter in word

#print(f"DEBUG:: Word: {word}") # Uncomment to see answer when program starts

step = 0
while step < 6:
    draw(step,wrong,board,word) # Draw current boardstate
    letter = guess(board+wrong) # collects guess and sets to letter
    if letter in word:
        board = vanna(board,letter,word) # Reveals letters on board
        if board == word:
            print(f"YOU WIN!!\nThe word was {word}")
            break
    else:
        print(f"{letter} is incorrect!")
        wrong += letter # Appends letter to wrong answer board
        step += 1
if step == 6:
    draw(step,wrong,board,word)
    print(f"YOU LOSE!!!\nThe word was {word}")






