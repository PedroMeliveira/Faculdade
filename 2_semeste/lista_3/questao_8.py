def Escreve(num):
    if num == 0:
        return 0
    return Escreve(num - 1) + num

print(Escreve(5))