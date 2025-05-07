frequencia = [0, 0, 0]
lista = [1, 4, 5]
qnt = 3
for num in lista:
    frequencia[num] += 1
soma = 0
i = -1
while soma < qnt / 2:
    i += 1
    soma += frequencia[i]
if qnt mod 2 = 1:
    return i
pos_mediana = i
while frequencia[i] = 0:
    i += 1
return (pos_mediana + i)/2
    