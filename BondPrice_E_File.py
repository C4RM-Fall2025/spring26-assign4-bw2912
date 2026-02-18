def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    m = len(yc)
    bondPrice = 0.0
    for t, y in enumerate(yc, start=1):
        cf = coupon + face if t == m else coupon
        bondPrice += cf / (1 + y) ** t
    return(bondPrice)
