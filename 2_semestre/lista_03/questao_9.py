# função A(m, n: inteiro): inteiro
# inicio
#     se m = 0 entao
#         retorne n + 1
#     fim se
#     se n = o entao
#         retorne A(m - 1, 1)
#     fim se
#     retorne A(m - 1, A(m, n - 1))
# fim função

# def A(m,n):
#     if m == 0:
#         return n + 1
#     if n == 0:
#         return A(m - 1, 1)
#     return A(m - 1, A(m, n - 1))


# print(A(5,4))

# função Tam(n: inteiro): inteiro
#     inicio
#         se n div 10 = 0 entao
#             retorne 1
#         fim se
#         retorne 10 * (Tam(n div 10))

def tam(num):
    if num // 10 == 0:
        return 1
    return 10 * tam(num // 10)

print(tam(9))