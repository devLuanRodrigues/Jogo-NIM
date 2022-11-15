def computador_escolhe_jogada(n, m):
    cpuRemove = 1
    while cpuRemove != m:
        if (n - cpuRemove) % (m+1) == 0:
            return cpuRemove
        else:
            cpuRemove += 1
    return cpuRemove

def usuario_escolhe_jogada(n, m):
    jogadaValida = False
    while not jogadaValida:
        playerRemove = int(input('Quantas peças você irá tirar? '))
        if playerRemove > m or playerRemove < 1:
            print()
            print('Oops! Jogada  inválida! Tente de novo.')
            print()
        else:
            jogadaValida = True
    return playerRemove

def campeonato():
    rodada = 1
    while  rodada <= 3:
        print()
        print('**** Rodada', rodada, '****')
        print()
        partida()
        rodada += 1
    print('**** Final do Campeonato! ****')
    print()
    print('Placar: Player 0 X 3 Computador')

def partida():
    n = int(input('Quantas peças? '))
    m= int(input('Limite de peças por jogada? '))
    vezCPU = False
    if n % (m+1) == 0:
        print()
        print('Você começa!')
    else:
        print()
        print('Computador começa!')
        vezCPU = True
    while n > 0:
        if vezCPU:
            cpuRemove = computador_escolhe_jogada(n, m)
            n = n - cpuRemove
            if cpuRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', cpuRemove, 'peças')
            vezCPU = False
        else:
            playerRemove = usuario_escolhe_jogada(n, m)
            n = n - playerRemove
            if playerRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', playerRemove, 'peças')
            vezCPU = True
        if n == 1:
            print('Agora resta apensa uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()
    print('Fim de jogo! O computador ganhou!')

print('bem vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')
tipoDePartida = int(input('2 - para jogar um campeonato'))
if tipoDePartida == 2:
    print()
    print('Você escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()
        
