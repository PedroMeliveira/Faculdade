s = 'OAALA'
t = 'A'
if len(s) == 0 or len(t) > len(s):
    print(0)
i = 0
j = 0
encontrou = False
while i <= (len(s) - 1) and j <= (len(t) - 1):
    if s[i] == t[j]:
        j += 1
        if not encontrou:
            posição = i 
        encontrou = True
    else:
        j = 0
        posição = 0
        encontrou = False
    i += 1
if encontrou and j > (len(t) - 1):
    print(posição)
else:
    print('deu ruim')
