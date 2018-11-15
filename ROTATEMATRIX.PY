def recall_password(cipher_grille, ciphered_password):
    passw=''
    for z in range(4):
        passw += "".join([ciphered_password[n][j] for n, i in enumerate(cipher_grille) for j, c in enumerate(i) if c =='X'])
        cipher_grille = tuple(zip(*cipher_grille[::-1]))
    return passw

import copy
def rotateMatrix(matrix):
    tmp = copy.deepcopy(matrix)
    for i in range(4):
        for x in range(4):
            tmp[x][3-i] = matrix[i][x]
    return tmp


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
