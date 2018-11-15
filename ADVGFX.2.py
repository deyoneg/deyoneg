from collections import OrderedDict
from itertools import zip_longest, chain

import numpy as np

CIPHER = 'ADFGVX'
N = len(CIPHER)

def encode(message, secret_alphabet, keyword):
    square = np.asarray(list(secret_alphabet)).reshape((N, N))

    frac = []
    for ch in ''.join(filter(str.isalnum, message.lower())):
        rows, cols = np.where(square == ch)
        frac.append(f"{CIPHER[rows[0]]}{CIPHER[cols[0]]}")

    frac = list(''.join(frac))
    key = "".join(OrderedDict.fromkeys(keyword))
    pad = len(key) - len(frac) % len(key)
    frac += [''] * pad
    table = np.asarray(frac).reshape(len(frac) // len(key), len(key))

    assoc = {c: table[:, i].tolist() for i, c in enumerate(key)}
    return ''.join([''.join(assoc[s]) for s in sorted(assoc)])

def decode(message, secret_alphabet, keyword):
    square = np.asarray(list(secret_alphabet)).reshape((N, N))

    key = "".join(OrderedDict.fromkeys(keyword))
    cols = {key[i]: len(message) // len(key) for i in range(len(key))}
    for i in range(len(message) % len(key)):
        cols[key[i]] += 1

    m = list(message)
    table = {}
    for c in sorted(key):
        table[c] = m[:cols[c]]
        m = m[cols[c]:]

    frac = [table[c] for c in key]

    codes = ''.join(x for x in chain.from_iterable(zip_longest(*frac)) if x is not None)
    coords = [codes[i:i+2] for i in range(0, len(codes), 2)]

    return ''.join(square[CIPHER.index(c1), CIPHER.index(c2)] for c1, c2 in coords)


if __name__ == "__main__":
    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"

    # assert encode("attack at 12:00 am",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"

    # assert encode("ditiszeergeheim",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"

    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"

    # assert (
    #     decode("FXGAFVXXAXDDDXGA", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "cipher")
    #     == "iamgoing"
    # ), "decode I am going"
    assert (
        decode(
            "DGDDDAGDDGAFADDFDADVDVFAADVX",
            "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
            "privacy",
        )
        == "attackat1200am"
    ), "decode attack"
    assert (
        decode(
            "DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
            "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
            "piloten",
        )
        == "ditiszeergeheim"
    ), "decode ditiszeergeheim"
    assert (
        decode("DXGAXAAXXVDDFGFX", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "weasel")
        == "iamgoing"
    ), "decode weasel == weasl"

