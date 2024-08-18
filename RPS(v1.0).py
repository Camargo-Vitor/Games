from random import randint
draw = playerPoints = computerPoints = 0

color = {
    'purple':"\033[0;35m",
    'dark_gray':"\033[1;30m",
    'green':"\033[0;32m",
    'yellow':"\033[0;33m",
    'cyan':"\033[0;36m",
    'nocolor':"\033[0m",
    'red':"\033[0;31m",
}

while True: 
    computerChoice = randint(1, 3) # 1 - rock   | 2 - paper | 3 - scissors
    print(color["dark_gray"]+'='*40)
    print(f'{color["cyan"]}[1] - ROCK \n[2] - PAPER \n[3] - SCISSORS{color["nocolor"]}')
    while True:
        try:
            playerChoice = int(input(f'{color["yellow"]}Choose your weapon (1, 2 or 3): {color["nocolor"]}'))
            if playerChoice in (1, 2, 3):
                break
            print(f'{color["red"]}Please choose a VALID WEAPON (1, 2 or 3) {color["nocolor"]}')
        except:
            print(f'{color["red"]}Please choose a VALID WEAPON (1, 2 or 3) {color["nocolor"]}')

#>>>>>> POSSIBLE MATCHES

    print(color["dark_gray"]+'='*40)
    if playerChoice == computerChoice:
        draw += 1
        print(f"{color['purple']}Computer chose {color['yellow']}>>{'ROCKS' if computerChoice == 1 else 'PAPER' if computerChoice == 2 else 'SCISSORS'}<< {color['purple']}for the battle")
        print(f"{color['dark_gray']}It's a draw! {color['nocolor']}")

    elif computerChoice == 3:  
        print(f'{color["purple"]}' + 'Computer chose' + f'{color["yellow"]}' + ' >>SCISSORS<< ' + f'{color["purple"]}for the battle' + f'{color["nocolor"]}')     
        if playerChoice == 1:       # player ROCK
            playerPoints += 1
            print(f'{color["green"]}Player wins {color["nocolor"]}')
        elif playerChoice == 2:     # player PAPER
            computerPoints += 1     
            print(f'{color["red"]}Computer wins {color["nocolor"]}')   
    elif computerChoice == 2:
        print(f'{color["purple"]}' + 'Computer chose' + f'{color["yellow"]}' + ' >>PAPER<< ' + f'{color["purple"]}for the battle' + f'{color["nocolor"]}')     
        if playerChoice == 1:       
            computerPoints += 1     
            print(f'{color["red"]}Computer wins {color["nocolor"]}') 
        elif playerChoice == 3:     # player SCISSOR
            playerPoints += 1
            print(f'{color["green"]}Player wins {color["nocolor"]} ')
    elif computerChoice == 1:
        print(f'{color["purple"]}' + 'Computer chose' + f'{color["yellow"]}' + ' >>ROCK<< ' + f'{color["purple"]}for the battle' + f'{color["nocolor"]}')           
        if playerChoice == 2:       # player PAPER
            playerPoints += 1 
            print(f'{color["green"]}Player wins {color["nocolor"]} ')       
        elif playerChoice == 3:     # player SCISSORS
            computerPoints += 1 
            print(f'{color["red"]}Computer wins {color["nocolor"]}') 
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    while True:
        try:
            cont = input(f'{color["yellow"]}Once more? [Y/N]: {color["nocolor"]}').upper()
            if cont[0] in 'YN':
                break
            print(f'{color["red"]}Insert a valid answer [YES(Y) OR NO(N)]{color["nocolor"]}')
        except:
            print(f'{color["red"]}Insert a valid answer [YES(Y) OR NO(N)]{color["nocolor"]}')
    if cont[0] == 'N':
        break


print(color['purple'] + '='*40)
print('FINAL SCORE'.center(40))
print('='*40, color['nocolor'])
print(f'{color["green"]}' + f'PLAYER POINTS: \t{playerPoints}'.expandtabs(38))
print(f'{color["red"]}' + f'COMPUTER POINTS: \t{computerPoints}'.expandtabs(38))
print(f'{color["nocolor"]}' + f'DRAWS: \t{draw}'.expandtabs(38))
