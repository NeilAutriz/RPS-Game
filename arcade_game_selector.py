import rps_game
import userGreeting
import guessing_game

# Main program menu.
def startGameSelection():
    userGreeting.startGreeting()
    print('MAIN MENU'.center(30, '*'))
    print('[1] 🎮Play Rock, Paper, and Scissors🎮')
    print('[2] 🔢Guessing Number Game🔢')
    print('[0] Exit the Program')
    game_choice = int(input('Enter your game choice: '))

    if game_choice == 1: 
        rps_game.playGame()
    elif game_choice == 2:
        guessing_game.playGuessGame()
    else:
        print('Please try again a valid option🎮')

if __name__ == '__main__':
    startGameSelection()