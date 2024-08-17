turno = X_wins = O_Wins = draws = 0 
vencedor = ''
cor = {
    'cinzao':"\033[1;30m",
    'verde':"\033[0;32m",
    'amarelo':"\033[0;33m",
    'ciano':"\033[0;36m",
    'semcor':"\033[0m",
    'vermelho':"\033[0;31m",
}

velha = [
    ['/', 'A', 'B', 'C'],
    ['1', ' ', ' ', ' '],
    ['2', ' ', ' ', ' '],
    ['3', ' ', ' ', ' ']
]


def tabela():
    for l in range(0,4):
        for c in range(0,4):
            print(f'{cor["ciano"]}[{velha[l][c]}]{cor["semcor"]}', end='')
        print()


def jogadalinha():
        while True:
            try:
                jlinha = int(input('Digite a linha: (1, 2, 3): '))
                if jlinha in (1, 2, 3):
                    return jlinha
                print(f'{cor["vermelho"]}Digite uma linha válida (1, 2, 3) {cor["semcor"]}')
            except:
                print(f'{cor["vermelho"]}Digite uma linha válida (1, 2, 3) {cor["semcor"]}')


def jogadacoluna():
        while True:
            jcoluna = str(input('Digite a coluna: (A, B, C): ')).upper()
            if jcoluna in ('A', 'B', 'C'):
                break
            print(f'{cor["vermelho"]}Digite uma linha válida (A, B, C) {cor["semcor"]}')
        if jcoluna == 'A':
            col = 1
        elif jcoluna == 'B':
            col = 2 
        elif jcoluna == 'C':
            col = 3
        return col

def fimdojogo(turno):
    #colunas

    if (velha[1][1] == velha[2][1] == velha[3][1] and velha[2][1] != ' '):
        return 'jogador'
    elif (velha[1][2] == velha[2][2] == velha[3][2] and velha[2][2] != ' '):
        return 'jogador'
    elif (velha[1][3] == velha[2][3] == velha[3][3] and velha[2][3] != ' '):
        return 'jogador'
    
    #linhas

    if (velha[1][2] == velha[1][2] == velha[1][3] and velha[1][2] != ' '):
        return 'jogador'
    elif (velha[2][1] == velha[2][2] == velha[2][3] and velha[2][2] != ' '):
        return 'jogador'
    elif (velha[3][1] == velha[3][2] == velha[3][3] and velha[3][2] != ' '):
        return 'jogador'
    
    #diagonais

    if (velha[1][1] == velha[2][2] == velha[3][3] and velha[2][2] != ' '):
        return 'jogador'
    elif (velha[1][3] == velha[2][2] == velha[3][1] and velha[2][2] != ' '):
        return 'jogador'
    
    #velha 

    if turno == 9:
        return 'empate'
    return ''


def resultadoPartida():
    if vencedor == 'empate':
        tabela()
        print(f'{cor["cinzao"]}EMPATE {cor["semcor"]}')
        return 'draw'
    else:
        if turno % 2 == 0:
            tabela()
            print(f'{cor["verde"]}VITÓRIA DA BOLINHA! {cor["semcor"]}')
            return 'O'
        else:
            tabela()
            print(f'{cor["verde"]}VITÓRIA DO XZINHO! {cor["semcor"]}')
            return 'X'

while True:
    while True:
        tabela()
        while True:
            jlinha = jogadalinha()
            col = jogadacoluna()
            if turno % 2 == 0:
                if velha[jlinha][col] == ' ':
                    velha[jlinha][col] = f'{cor["vermelho"]}X{cor["ciano"]}'
                    turno += 1
                    break
            elif turno % 2 != 0:
                if velha[jlinha][col] == ' ':
                    velha[jlinha][col] = f'{cor["amarelo"]}O{cor["ciano"]}'
                    turno += 1
                    break
            print(f'{cor["vermelho"]}Esse posição já está preenchida, escolha outra jogada {cor["semcor"]}')
        vencedor = fimdojogo(turno)
        if vencedor != '':
            break 
    round = resultadoPartida()    
    if round == 'draw':
        draws += 1
    elif round == 'O':
        O_Wins += 1
    elif round == 'X':
        X_wins += 1
    cont = input('Quer continuar jogando? [S/N]').upper()
    if cont in 'N':
        break
    else:
        turno = 0
        velha = [
        ['/', 'A', 'B', 'C'],
        ['1', ' ', ' ', ' '],
        ['2', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ']
    ]
print('RESULTADOS: ')
print(f'VITÓRIAS [O]: {O_Wins}')
print(f'VITÓRIAS [X]: {X_wins}')
print(f'EMPATES: {draws}')
