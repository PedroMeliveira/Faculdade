def maior_valor(flag):
    num =  float(input(''))
    if num == flag:
        return num
    
    maior = maior_valor(flag)
    if num > maior or maior == flag:
        return num
    return maior

print(maior_valor(10))