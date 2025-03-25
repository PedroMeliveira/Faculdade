def Anagrama(s, t):
    def ana(ns):
        def Q(r, m):
            if m == -1:
                return 0
            if s[ns] == r[m]:
                return 1 + Q(r, m - 1)
            else:
                return Q(r, m - 1)
        if ns == -1:
            return True
        else:
            return (Q(s, len(s)- 1) == Q(t, len(t) - 1)) and ana(ns - 1)
    if (s == t) or (len(s) != len(t)):
        return False
    return ana(len(s) - 1)


s = 'abaa'
t = 'abaa'

print(Anagrama(s, t))
        