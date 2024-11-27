# This contains the guessing game which can be customized by the user's name.
# Counts games, wins, and winning percentage.
# Continuously plays the game then connects it.

import random
import userGreeting

def playGuessGame():
    gameResults = {
    "playerWins": 0,
    "matchTotal": 0,
    "totalGuesses": 0
    }
    userGreeting.startGreeting()
    if(userGreeting.arguments.name == None):
        userName = 'User'
    else:
        userName = userGreeting.arguments.name
    if(userGreeting.arguments.language == None):
        userLanguage = 'English'
    else:
        userLanguage = userGreeting.arguments.language
    showMainMenu(gameResults, userName)
    
# Main program menu.
def showMainMenu(gameResults, userName):
    print('GUESSING GAME'.center(30, '*'))
    print('[1] Play the number guessing game')
    print('[2] Show Match Results')
    print('[0] Exit the Program')
    userChoice = getUserChoice()
    if(userChoice == 1):
        guessingGame(gameResults, userName)
    elif(userChoice == 2):
        guessingResult(gameResults, userName)
    elif(userChoice == 0):
        print('Thank you for using the program!')
    else:
        print(f"{userName}, Enter a valid number from the choices.")

#getting the input of the user
def getUserChoice():
    userChoice = int(input('Enter your choice: '))
    return userChoice

# Game logic for the guessing game.
def guessingGame(gameResults, userName):
    number_choices = [x for x in range(1, 101)]
    print('🧠 Welcome to the guessing game 🧠')
    print(f"Hello! {userName}😁, am thinking of a number between 1-100🤯")
    userGuess = getGuess(number_choices)
    while(userGuess not in number_choices):
        userGuess = getGuess(number_choices)
    correctAnswer = random.choice(number_choices)

    print(userGuess, correctAnswer)
    gameLogic(gameResults, userGuess, correctAnswer, number_choices, userName)
    

def guessingResult(gameResults, userName):
    if(gameResults['matchTotal'] == 0):
        print('No matches yet📪')
        showMainMenu(gameResults, userName)
    print(f"{userName} Total Matches: {gameResults['matchTotal']}🎮")
    print(f"{userName} Wins: {gameResults['playerWins']}🥂")
    playerRatings = round(int(gameResults['playerWins'])/int(gameResults['totalGuesses']) * 100, 2)
    print(f"{userName} Ratings: {playerRatings}%👌")
    showMainMenu(gameResults, userName)

def gameLogic(gameResults, userGuess, correctAnswer, number_choices, userName):
    gameResults['matchTotal'] += 1
    gameResults['totalGuesses'] += 1
    while(userGuess != correctAnswer):
        if(userGuess > correctAnswer):
            print(f"{userName} guess is higher than the number.")
            userGuess = getGuess(number_choices)
            gameResults['totalGuesses'] += 1
        elif(userGuess < correctAnswer):
            print(f"{userName} answer is way too low.")
            userGuess = getGuess(number_choices)
            gameResults['totalGuesses'] += 1
        else:
            print(f"{userName}Please enter a valid number within the specified range (1-100)")
    
    print(f"{userName} have successfully guessed the number!")
    gameResults['playerWins'] += 1
    print(gameResults)
    showMainMenu(gameResults, userName)

def getGuess(number_choices):
    getGuess = int(input("Enter another guess: "))
    while(getGuess not in number_choices):
        getGuess = int(input("Enter a valid guess based on the specified limit [1-100]: "))
    return getGuess    



if __name__ == '__main__':
    playGuessGame()