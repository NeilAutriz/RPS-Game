import rps_game
import userGreeting

# Main program menu.
def startGameSelection():
    userGreeting.startGreeting()
    print('MAIN MENU'.center(30, '*'))
    print('[1] Play Rock, Paper, and Scissors')
    print('[2] Snack and Ladders'   )
    print('[3] Tik-Tak-Toe')
    print('[0] Exit the Program')
    game_choice = int(input('Enter your game choice: '))

    if game_choice == 1:
        rps_game.playGame()
    else:
        print('Please try again a valid option🎮')

if __name__ == '__main__':
    startGameSelection()