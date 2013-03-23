def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    elif a > b:
        r = a % b
        if r == 0:
            return b
        else:
            # print r, b
            return gcd(b, r)
    elif b > a:
        a, b = b, a
        return gcd(a,b)


#print gcd(0, 4)
#print gcd(4, 0)
#print gcd(4, 2)
#print gcd(21, 9)
#print gcd(13, 17)
#print gcd(125, 4300)
