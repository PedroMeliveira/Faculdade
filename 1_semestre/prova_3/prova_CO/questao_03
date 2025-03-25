algoritmo           String_Alternada_Letra_Digito
var
    s: string 
    i: inteiro
    alterna: lógico
inicio
    escreva("Digite uma string: ")
    leia(s)
    se tamanho(s) < 3 entao
        escreva("Sucesso")
    senao
    i <- 2      
    alterna <- VERDADEIRO
    enquanto i <= tamanho(s) e alterna faça
        se não ((('a' <= s[i - 1] e s[i - 1] <= 'z') ou ('A' <= s[i - 1] e s[i-1] <= 'Z')) e ('0' <= s[i] e s[i] <= '9')) entao 
            se não ((('a' <= s[i] e s[i] <= 'z') ou ('A' <= s[i] e s[i] <= 'Z')) e ('0' <= s[i - 1] e s[i - 1]<= '9')) entao
                alterna <- FALSO
            fim se
        fim se
        i <- i + 1
    fim enquanto
    se alterna entao
        escreva("Sucesso")
    senao
        escreva("Falha")
    fim se
fim algoritmo