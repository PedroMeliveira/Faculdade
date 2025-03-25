algoritmo Transforma_String_Em_Inteiro
var
    s: string
    num, i, negativo: inteiro
    apenas_num: lógico
inicio
    escreva("Digite uma string: ")
    leia(s)
    se s = "" entao
        escreva("String vazia, não foi possível fazer a transformação.")
    senao 
        i <- 1
        se s[i] = "-" entao
            negativo <- -1
            i <- 2
        senao
            negativo <- 1
        fim se
        apenas_num <- VERDADEIRO
        num <- 0
        enquanto i <= tamanho(s) e apenas_num faça
            se '0' <= s[i] e s[i] <= '9' entao
                num <- num * 10 + asc('0') - asc(s[i])
            senao
                apenas_num <- FALSO
            fim se
            i <- i + 1
        fim enquanto
        se apenas_num entao
            escreva(num * negativo)
        senao
            escreva("Entrada inválida, não tem apenas dígitos nessa string!")
        fim se
    fim se
fim algoritmo
