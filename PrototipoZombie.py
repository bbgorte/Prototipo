#Início do jogo
import random

print("-"*30, "\n   BEM VINDO AO ZOMBIE DICE\n", "-"*30)

#Número de jogadores: precisa ser maior do que 1
numJogadores = int(input("Em quantos zumbis nós vamos jogar hoje?? "))
if numJogadores < 2:
    print("Precisamos de mais zumbis!!")
    while numJogadores < 2:
        numJogadores = int(input("Quantos zumbis vão caçar?"))

#Lista para guardar o nome de cada jogador
listaJogadores = []
for i in range(numJogadores):
    nome = input(f"Informe nome do {str(i+1)} zumbi: ")
    if nome == "":
        print("Precisamos do seu nome para identificar!!")
        while nome == "":
            nome = input("Por favor, informe seu nome de zumbi!")

    listaJogadores.append(nome)
    print(listaJogadores)

#embaralhar os jogadores para a ordem de jogo:
random.shuffle(listaJogadores)
print(f"A ordem aleatória para jogar é: {listaJogadores}")

#lista dos dados
verde = "CPCTPC"
amarelo = "TPCTPC"
vermelho = "TPTCPT"

dadosTubo = [verde, verde, verde, verde, verde, verde, amarelo, amarelo, amarelo, amarelo, vermelho, vermelho, vermelho]


#iniciar o jogo
jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

while True:
    print(f"\nTURNO DO JOGADOR {listaJogadores[jogadorAtual]}\n")

    #sortear 3 dados aleatórios do tubo

    for i in range(0, 3):
        numSorteado = random.choice(dadosTubo)

        if numSorteado == 'CPCTPC':
            corDado = 'VERDE'
            print(f'DADO SORTEADO: {corDado}')

        if numSorteado == 'TPCTPC':
            corDado = 'AMARELO'
            print(f'DADO SORTEADO: {corDado}')

        if numSorteado == 'TPTCPT':
            corDado = 'VERMELHO'
            print(f'DADO SORTEADO: {corDado}')

        dadosSorteados.append(numSorteado)


    #sorteio das faces dos 3 dados
    print("As faces sorteadas foram: ")

    #nFace é o numero da face do dado
    for dadoSorteado in dadosSorteados:
        nFace = random.randint(0, 5)

        if dadoSorteado[nFace] == "C":
            print("FACE: C")
            print("Você comeu um cérebro!!")
            cerebros += 1

        if dadoSorteado[nFace] == "T":
            print("FACE: T")
            print("Ah não!! Você levou um tiro!")
            tiros += 1

        if dadoSorteado[nFace] == "P":
            print("FACE: P")
            print("Sua vítima fugiu!")

    if cerebros >= 13:
        print(f"VOCÊ COMEU {cerebros} CEREBROS, VENCEU A PARTIDA!!!")
        break

    if tiros >= 3:
        print("VOCÊ LEVOU 3 TIROS! VOLTE NA PRÓXIMA RODADA")
        jogadorAtual += 1
        dadosSorteados = []
        tiros = 0
        cerebros = 0

        if (jogadorAtual == len(listaJogadores)):
            print("FINALIZANDO RODADA")
            jogadorAtual = 0
        continue

    #imprimir o placar:
    print("-"*20, "\n       SCORE\n", "-"*20)
    print(f"CÉREBROS ACUMULADOS: {cerebros} \n TIROS DA RODADA: {tiros}\n")

    #perguntar para o jogador se deseja jogar os dados novamente
    if tiros <= 3:
        repetir = input("Quer arriscar os dados novamente? s/n: ")

    if repetir == "n":
        jogadorAtual += 1
        dadosSorteados = []
        tiros = 0

        if (jogadorAtual == len(listaJogadores)):
            print("FINALIZANDO RODADA")
            jogadorAtual = 0

    else:
        print("Iniciando mais uma rodada do turno")
        dadosSorteados = []





