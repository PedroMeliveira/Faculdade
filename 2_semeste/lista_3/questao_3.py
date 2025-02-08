def Reverso(num):
    def Tamanho_num(num):
        if (num // 10) == 0:
            return 1
        else:
            return Tamanho_num(num // 10) * 10
        
    if num < 0:
        neg = -1
        num = -num
    else:
        neg = 1

    if (num // 10) == 0:
        return num
    return (num % 10 * Tamanho_num(num) + Reverso(num // 10)) * neg

print(Reverso(-1234))