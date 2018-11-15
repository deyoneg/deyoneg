import math


def encode(message, secret_alphabet, keyword):

    # remove duplicated symbols in keyword
    keyword = "".join(sorted(set(keyword), key=keyword.index))
    print(keyword)

    # clean message
    message = message.replace(" ", "").lower()

    # grouping secret alphabet
    coords = "ADFGVX"
    res = [
        secret_alphabet[i : i + len(coords)]
        for i in range(0, len(secret_alphabet), len(coords))
    ]
    print(res)

    # get coordinates
    coo = []
    for s in message:
        for i in range(len(res)):
            j = res[i].find(s)
            if j != -1:
                coo.append(coords[i] + coords[j])
                break
    coo = "".join(coo)
    print((coo))

    # grouping coordinates by keyword
    res = [coo[i : i + len(keyword)] for i in range(0, len(coo), len(keyword))]
    print("res", res)

    # link column to symbol in keyword
    dic = {}
    for i, c in enumerate(keyword):
        temp = ""
        for j in res:
            try:
                temp += j[i]
            except IndexError:
                pass
        dic[c] = temp
    print(dic)

    # sort keyword dictionary and create encoded string
    sorteddic = sorted(dic.keys())
    print(str(sorteddic))
    out = ""
    for i in sorteddic:
        out += dic[i]
    print(out)
    return out


import math


def decode(message, secret_alphabet, keyword):
    # remove duplicated symbols in keyword
    keyword = "".join(sorted(set(keyword), key=keyword.index))
    print(keyword)


    rows = int(math.ceil(len(message) / len(keyword)))
    fullcells = len(keyword) if not(len(message) % len(keyword)) else len(message) % len(keyword)

    dictt = {}
    for i in keyword:
        dictt[i] = [""] * rows

    ddd = {
        c: [""] * rows if x < fullcells else [""] * (rows - 1)
        for x, c in enumerate(keyword)
    }
    print(ddd)

    sortedkeyword = sorted(keyword)
    print(sortedkeyword)

    pos = 0
    for j in sortedkeyword:
        ddd[j] = message[pos : pos + len(ddd[j])]
        pos += len(ddd[j])
    print(ddd)

    # get coords
    out = ""
    for y in range(len(ddd[keyword[0]])):
        for i in keyword:
            try:
                out += ddd[i][y]
            except:
                pass
    print(out)

    coords = "ADFGVX"
    res = [
        secret_alphabet[i : i + len(coords)]
        for i in range(0, len(secret_alphabet), len(coords))
    ]
    print(res)

    mes = ""

    for i in [out[z : z + 2] for z in range(0, len(out), 2)]:
        mes += res[coords.index(i[0])][coords.index(i[1])]
    print(mes)
    return mes


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

