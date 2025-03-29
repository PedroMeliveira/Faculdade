algoritmo           Troca_Bit_Caracter
var
    c:  caracter
    alg2, alg7, num: inteiro
inicio
    escreva("Digite um caracter: ")
    leia(c)
    num <- asc(c)
    alg7 <- (num div 2) mod 2
    alg2 <- (num div 64) mod 2
    num <- num - (alg7 * 2) + (alg2 * 2) - (alg2 * 64) + (alg7 * 64)
    decimal <- + (alg2 * 2) + num div 4 mod 16
    escreva(chr(num))
fim algoritmo