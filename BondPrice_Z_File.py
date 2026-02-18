def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    t_max = max(times)
    bondPrice = 0.0
    for t, y in zip(times, yc):
        cf = coupon + face if t == t_max else coupon
        bondPrice += cf / (1 + y) ** t
    return(bondPrice)
