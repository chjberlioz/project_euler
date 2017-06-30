def GetPalindromic(n):
    return int(''.join(list(str(n))[::-1]))


def IsPalindromic(n):
    return n == GetPalindromic(n)


def IsLychrel(n):
    cc = 0
    n = n + GetPalindromic(n)
    while cc <= 50:
        if IsPalindromic(n):
            return False
        n = n + GetPalindromic(n)
        cc += 1
    return True


result = filter(IsLychrel, range(10001))
print len(result)