import random
import userGreeting

gameChoices = ['🪨', '📄', '✂️']
gameIndex = [0, 1, 2]

def playGame():
    userName = userGreeting.arguments.name
    if(userName == 'None'):
        userName = 'User'
    else:
        userName = userGreeting.arguments.name
    game_records = {
        "matchCount": 0,
        "winCount": 0,
        "loseCount": 0,
        "drawCount": 0
    }
    while True:
        showMainMenu(userName)
        userChoice = int(getUserInput())
        if userChoice > 2 or userChoice < 0:
            print('Enter a valid user choice😔')
        elif userChoice == 2:
            showMatchHistory(game_records, userName)
        elif userChoice == 0:
            print('Thank you for using the program! 💻')
            break
        else:
            while True:
                showGameChoices()
                userSelection = int(getUserInput())
                if userSelection == 3:
                    print('Exiting the game❌')
                    break
                else:
                    userSelection = convertUserSelection(userSelection)
                    computerSelection = getComputerSelection()
                    gameLogic(userSelection, computerSelection, game_records)

# Show match history.
def showMatchHistory(game_records, userName):
    print(f"{userName} Game History".center(30, '*'))
    print(f"🎮{userName}Total Matches Count: ", game_records["matchCount"])
    print(f"🏆{userName} Win Count: ", game_records["winCount"])
    print(f"{userName}❌ Lose Count: ", game_records["loseCount"])
    print(f"{userName}👌 Draw Count: ", game_records["drawCount"])

# Convert user selection.
def convertUserSelection(userSelection):
    userSelection = gameChoices[userSelection]
    print('User choice: ', userSelection)
    return userSelection

# Obtain the computer's choice.
def getComputerSelection():
    computerSelection = random.choice(gameChoices)
    print('Computer choice: ', computerSelection)
    return computerSelection

# Main program menu.
def showMainMenu(userName):
    print(f"🎮{userName}, welcome to the RPS GAME🎮")
    print('RPS GAME'.center(30, '*'))
    print('[1] Play Rock, Paper, and Scissors')
    print('[2] Show Match Results')
    print('[0] Exit the Program')

# Game choices menu.
def showGameChoices():
    print('GAME CHOICES'.center(30, '*'))
    print('[0] Rock 🪨')
    print('[1] Paper 📄')
    print('[2] Scissors ✂️')
    print('[3] Exit the Game 😭')

# Obtain user input.
def getUserInput():
    userInput = input('Enter your choice: ')
    return userInput

# Game logic and updating match counts.
def gameLogic(userSelection, computerSelection, game_records):
    game_records['matchCount'] += 1

    if userSelection == computerSelection:
        print('👌The match is a draw.')
        game_records['drawCount'] += 1
    elif (userSelection == '✂️' and computerSelection == '📄') or \
         (userSelection == '📄' and computerSelection == '🪨') or \
         (userSelection == '🪨' and computerSelection == '✂️'):
        print('✅You have won the match.')
        game_records['winCount'] += 1
    else:
        print('❌You have lost the match.')
        game_records['loseCount'] += 1
    print('Match Count:', game_records["matchCount"], 'Wins:', game_records["winCount"], 
          'Losses:', game_records["loseCount"], 'Draws:', game_records["drawCount"])
    
    return playGame


if __name__ == '__main__':
    # Start the game.
    playGame()