from random import randrange

def imprimirTabuleiro(tabuleiro):
	print("+-------" * 3,"+", sep="")
	for linha in range(3):
		print("|       " * 3,"|", sep="")
		for coluna in range(3):
			print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def jogadaLivre(tabuleiro, jogada, jogadas):
	if tabuleiro.count(jogada) == 0:
		tabuleiro.append(jogada)
		return True
	else:
		return False

def fazerJogada(tabuleiro, jogada, indice):
	if jogada <= 3:
		x = 0
		y = jogada - 1
	elif jogada >= 4 and jogada <= 6:
		x = 1
		y = jogada - 4
	elif jogada >= 7:
		x = 2
		y = jogada - 7
	if indice % 2 == 0:
		tabuleiro[x][y] = "X"
	else:
		tabuleiro[x][y] = "O"
	return tabuleiro

def vitoriaMensagem(indice):
	if indice % 2 != 0:
		print("================")
		print("  Você Perdeu!  ")
		print("================")
	else:
		print("================")
		print("  Você Venceu!  ")
		print("================")

def empate(contador):
	if contador == 10:
		print("=================")
		print("     Empate!     ")
		print("=================")

def vitoria(tabuleiro):
	if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]:
		return True
	elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]:
		return True
	elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]:
		return True
	elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
		return True
	elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
		return True
	elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
		return True
	elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
		return True
	elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
		return True
	else:
		return False

tabuleiro = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

jogadas = []

imprimirTabuleiro(tabuleiro)
indice = 1
contador = 1
reiniciar = True
while reiniciar:
	reiniciar = False
	while True:
		if indice % 2 == 0:
			jogada = randrange(8)
			jogada = jogada + 1
		else:
			jogada = int(input("Informe a sua jogada: "))
		if jogadaLivre(tabuleiro, jogada, jogadas) == False:
			reiniciar = True
			break
		fazerJogada(tabuleiro, jogada, indice)
		imprimirTabuleiro(tabuleiro)
		indice = indice + 1
		contador = contador + 1
		if vitoria(tabuleiro):
			vitoriaMensagem(indice)
			break
		empate(contador)