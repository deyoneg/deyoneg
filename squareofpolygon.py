def checkio(coo):
    coo.append(coo[0])
    x, y = map(list, zip(*coo))
    square = (sum([a*b for a,b in zip(x[1:],y[:-1])])-sum([a*b for a,b in zip(x[:-1],y[1:])]))/2
    return abs(square)

def checkio2(a):
    return abs(sum([x[0][0] * x[1][1] - x[1][0] * x[0][1] for x in zip(a, a[1:] + a[:1])]) / 2.0)

    checkio3 = lambda d: abs( sum( (d[i][0] * d[i+1][1] - d[i][1] * d[i+1][0]) for i in range(-1,len(d)-1)))/2

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
