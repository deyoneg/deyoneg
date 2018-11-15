dedupe = lambda k: [c for i, c in enumerate(k) if c not in k[:i]]

def polybius(sa, enc=True):
    letters ='ADFGVX'
    polybius_index = [c + letters[i % 6] for i, c in enumerate(''.join([6 * x for x in letters]))]
    if enc: return dict(zip(sa, polybius_index))
    else: return dict(zip(polybius_index, sa))

def alphebecipher(strng, kw):
    table, ciphered = [[] for i in range(len(kw))], []
    for i, char in enumerate(strng):
        table[i%len(kw)].append(char)
    table_dict = dict(zip(kw, table))
    for nc in [table_dict[c] for c in sorted(kw)]:
        ciphered.extend(nc)
    return ciphered

def encode(message, secret_alphabet, keyword):
    p = polybius(secret_alphabet)
    frac = ''.join([p[c] for c in list(message.lower()) if c in p])
    return ''.join(alphebecipher(frac, dedupe(keyword)))

def decode(message, secret_alphabet, keyword):
    p = polybius(secret_alphabet, False)
    frac = ''.join([c[1] for c in sorted(zip(alphebecipher(range(len(message)), dedupe(keyword)), message))])
    return ''.join([p[t] for t in [frac[i*2:i*2+2] for i in range(int(len(frac)/2))]])


if __name__ == "__main__":
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"

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

