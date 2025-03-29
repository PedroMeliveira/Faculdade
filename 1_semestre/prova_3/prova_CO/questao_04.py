algoritmo       Encontra_Posição_De_T_Em_S
var
    s, t: string
    i, j, posição: inteiro
    encontrou: lógico
inicio
    escreva("Digite 2 string: ")
    leia(s, t)
    se tamanho(s) = 0 ou tamanho(t) > tamanho(s) entao
        escreva(0)
    senao
    i <- 1
    j <- 1
    encontrou <- FALSO
    enquanto i <= tamanho(s) e j <= tamanho(t) faça
        se s[i] = t[j] entao 
            i <- i + 1
            j <- j + 1
            se nao encontrou entao
                posição <- i 
            fim se
            encontrou <- VERDADEIRO
        senao
            i <- i + 1
            j <- 1
            posição <- 0
            encontrou <- FALSO
        fim se
    fim enquanto
    se encontrou e j > tamanho(t) entao
        escreva(posição)
    senao
        escreva(0)
    fim se
fim algoritmo