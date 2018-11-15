def encode(msg, secret_alphabet, key):
    key, size, out = sorted(set(key), key=key.index), len(set(key)), ""
    for i in [x for x in msg.lower() if x.isalnum()]:
        a, b = divmod(secret_alphabet.find(i), 6)
        out += "ADFGVX"[a]+"ADFGVX"[b]
    out = [(out+" "*size)[size*x:size*(x+1)] for x in range(len(out)//size+1)]
    out = [x for _, x in sorted(zip(key, zip(*out)))]
    return ''.join([''.join(x) for x in out]).replace(' ', '')


def decode(msg, secret_alphabet, key):
    key, length, size = sorted(set(key), key=key.index), len(msg), len(set(key))
    out = [(x, length//size+1-(i >= length-length//size*size)) for i, x in enumerate(key)]
    out = [i for x, i in sorted(out)]
    out = [msg[sum(out[:i]):sum(out[:i])+x] for i, x in enumerate(out)]
    out = sorted([x for x in zip(sorted(set(key)), out)], key=lambda x: key.index(x[0]))
    out = __import__('itertools').zip_longest(*[x for _, x in out], fillvalue=' ')
    out = ["ADFGVX".find(x) for x in ''.join([''.join(x) for x in out]).replace(' ', '')]
    return ''.join([secret_alphabet[6*i+j] for i, j in zip(out[::2], out[1::2])])

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

