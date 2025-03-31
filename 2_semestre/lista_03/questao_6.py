def Qnts_B_em_A(a,b):
    if b // 10 != 0:
        return -1
    if a < 0 or b < 0:
        return -1
    if a == 0:
        return 0
    if a % 10 == b:
        return 1 + Qnts_B_em_A(a // 10, b)
    return Qnts_B_em_A(a // 10, b)

print(Qnts_B_em_A(123333312, 3))