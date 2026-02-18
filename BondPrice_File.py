def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy
    bondPrice = sum(c / (1 + r) ** t for t in range(1, n + 1))
    bondPrice += face / (1 + r) ** n
    return bondPrice