import argparse

def greetUser(name, language):
    languageGreeting={
        "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour",
        "Ciao": "Italian"
    }
    print(f"{languageGreeting[language]}, {name}😁")

parser = argparse.ArgumentParser(
    prog="RPS Game",
    description="This allows to provides the greeting to the players of the RPS Game."
)

parser.add_argument(
    '-name', '-n', help="Takes the name of the user of the game.", required=False
)

parser.add_argument(
    "-language", '-l', help="This determines what language the user actually utilizes", required=False
)

arguments = parser.parse_args()

def startGreeting():
    if(arguments.name == None or arguments.language == None):
        print(f"Hello there!😁")
    else:
        greetUser(arguments.name, arguments.language)

if(__name__ == '__main__'):
    startGreeting()