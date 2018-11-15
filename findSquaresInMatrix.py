from typing import List

def checkio(lines_list: List[List[int]]) -> int:
    c = 0
    lines_list = list(map(lambda x: sorted(x),lines_list))
    for m in range(1, 4):
        print ("m=",m)
        for i in range(1,16):
            if len([True for x in range(m) if [i + x, i + x + 1] in lines_list]) == m:
                if len([True for x in range(m) if [i + x * 4 + m, i + x * 4 + m + 4] in lines_list]) == m:
                    if len([True for x in range(m) if [i + x + m * 4, i + x + m * 4 + 1] in lines_list]) == m:
                        if len([True for x in range(m) if [i + x * 4, i + x * 4 + 4] in lines_list]) == m:
                            c += 1
    return c


if __name__ == '__main__':
    print("Example:")
    print(checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                      [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                      [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")