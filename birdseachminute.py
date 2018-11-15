def checkio(number):
    print ("--------",number,"----------")
    N = number
    c=0
    for i in range(number):
        i+=1
        c = c+i
        N = N - c
        if N == 0:
            break
        elif N < 0:
            c = max(c+N, c-i)
            break
    return c

def checkio(food):
    count = 1
    res = [0]
    while 1:
        for index in range(len(res)):
            res[index] += 1
            food -= 1
            if not food: return len(res) - res.count(0)
        count += 1
        res += [0] * count
        
def checkio(number):
    pig, i = 1, 1
    while number > 0:
        ans = max(pig-i, number)
        number -= pig
        i += 1
        pig += i
    return ans

if __name__ == '__main__':
    checkio(3)
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(10) == 6, "4th example"
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"