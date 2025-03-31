def bi_dec(num):
    if num == 0:
        return 0
    if num % 10 != 0 and num % 10 != 1:
        return -999999
    return num % 10 + 2 * bi_dec(num // 10)

print(bi_dec(10000))