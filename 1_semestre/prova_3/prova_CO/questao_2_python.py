numero = int(input(f'Digite um numero'))
alg7 = (numero // 2) % 2
alg2 = (numero // 64) % 2
print(alg7, alg2)
numero_invertido = numero - (alg7 * 2) + (alg2 * 2) - (alg2 * 64) + (alg7 * 64)

print(numero, numero_invertido)
