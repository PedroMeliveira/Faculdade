algoritmo       Acha_Qntd_Diferença_Bits_E_Primeiro_Bit
var
	c, k: caracter
	diferentes, posição, num_c, num_k: inteiro
inicio
	escreva("Digite 2 caracteres: ")
	leia(c, k)
	num_c <- asc(c)
	num_k <- asc(k)
	diferentes <- 0
	posição <- 0
	i <- 1
	enquanto i <= 8 faça
		se num_c mod 2 != num_k mod 2 entao
			diferentes <- diferentes + 1
			posição <- i 
		fim se
		num_c <- num_c div 2
		num_k <- num_k div 2
		i <- i + 1
	fim enquanto
	escreva("Quantidade de posições diferentes: ", diferentes)
	se diferentes > 0 entao
		escreva("Primeira posição diferente: ", posição)
	senao
		escreva("Não tem primeira posição diferente!")
	fim se
fim algoritmo
