def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy
    price = 0.0
    weighted = 0.0
    for t in range(1, n + 1):
        cf = c if t < n else c + face
        pv = cf / (1 + r) ** t
        price += pv
        weighted += t * pv
    bondDuration = (weighted / price) / ppy
    return bondDuration
