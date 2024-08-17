turn = X_wins = O_Wins = draws = 0 
winner = ''
color = {
    'purple':"\033[0;35m",
    'dark_gray':"\033[1;30m",
    'green':"\033[0;32m",
    'yellow':"\033[0;33m",
    'cyan':"\033[0;36m",
    'nocolor':"\033[0m",
    'red':"\033[0;31m",
}

table = [
    ['/', 'A', 'B', 'C'],
    ['1', ' ', ' ', ' '],
    ['2', ' ', ' ', ' '],
    ['3', ' ', ' ', ' ']
]


def printTable():
    for l in range(0,4):
        for c in range(0,4):
            print(f'{color["cyan"]}[{table[l][c]}]{color["nocolor"]}', end='')
        print()


def chosenLine():
        while True:
            try:
                pLine = int(input('Choose the line (1, 2 or 3): '))
                if pLine in (1, 2, 3):
                    return pLine
                print(f'{color["red"]}Type a valid line (1, 2 or 3) {color["nocolor"]}')
            except:
                print(f'{color["red"]}Type a valid line (1, 2 or 3) {color["nocolor"]}')


def chosenColumn():
        while True:
            pColumn = str(input('Type the column (A, B or C): ')).upper()
            if pColumn in ('A', 'B', 'C'):
                break
            print(f'{color["red"]}Type a valid column (A, B or C): {color["nocolor"]}')
        if pColumn == 'A':
            col = 1
        elif pColumn == 'B':
            col = 2 
        elif pColumn == 'C':
            col = 3
        return col


def Game_end(turn):
    #column possible wins

    if (table[1][1] == table[2][1] == table[3][1] and table[2][1] != ' '):
        return 'player'
    elif (table[1][2] == table[2][2] == table[3][2] and table[2][2] != ' '):
        return 'player'
    elif (table[1][3] == table[2][3] == table[3][3] and table[2][3] != ' '):
        return 'player'
    
    #line possible wins

    if (table[1][2] == table[1][2] == table[1][3] and table[1][2] != ' '):
        return 'player'
    elif (table[2][1] == table[2][2] == table[2][3] and table[2][2] != ' '):
        return 'player'
    elif (table[3][1] == table[3][2] == table[3][3] and table[3][2] != ' '):
        return 'player'
    
    #diagonal possible wins

    if (table[1][1] == table[2][2] == table[3][3] and table[2][2] != ' '):
        return 'player'
    elif (table[1][3] == table[2][2] == table[3][1] and table[2][2] != ' '):
        return 'player'
    
    #draw (full board)

    if turn == 9:
        return 'draw'
    return ''


def matchResult():
    if winner == 'draw':
        printTable()
        print(f'{color["dark_gray"]}DRAW {color["nocolor"]}')
        return 'draw'
    else:
        if turn % 2 == 0:
            printTable()
            print(f'{color["green"]}CIRCLE WINS! {color["nocolor"]}')
            return 'O'
        else:
            printTable()
            print(f'{color["green"]}X WINS! {color["nocolor"]}')
            return 'X'

while True:
    while True:
        printTable()
        while True:
            pLine = chosenLine()
            col = chosenColumn()
            if turn % 2 == 0:
                if table[pLine][col] == ' ':
                    table[pLine][col] = f'{color["red"]}X{color["cyan"]}'
                    turn += 1
                    break
            elif turn % 2 != 0:
                if table[pLine][col] == ' ':
                    table[pLine][col] = f'{color["yellow"]}O{color["cyan"]}'
                    turn += 1
                    break
            print(f'{color["red"]}This position is already taken. Choose another one! {color["nocolor"]}')
        winner = Game_end(turn)
        if winner != '':
            break 
    round = matchResult()    
    if round == 'draw':
        draws += 1
    elif round == 'O':
        O_Wins += 1
    elif round == 'X':
        X_wins += 1
    while True:
        cont = input('Do you want to keep playing? [Y/N]: ').upper()
        if cont[0] in 'YN':
            break
        print(f'{color["red"]}Please type Yes(Y) or No(N){color["nocolor"]}')
    if cont[0] in 'N':
        break
    else:
        turn = 0
        table = [
        ['/', 'A', 'B', 'C'],
        ['1', ' ', ' ', ' '],
        ['2', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ']
    ]

print(color['purple']+'='*30)
print(f'{color["purple"]}RESULTS'.center(35))
print('='*30, color['nocolor'])
print(f'{color["yellow"]}[O]' + f'{color["cyan"]} WINS: \t{O_Wins}'.expandtabs(32) + color["nocolor"]) 
print(f'{color["red"]}[X]' + f'{color["cyan"]} WINS: \t{X_wins}'.expandtabs(32) + color["nocolor"]) 
print(f'{color["dark_gray"]}[D]' + f'{color["cyan"]} DRAWS: \t{draws}'.expandtabs(32) + color["nocolor"])
