
#! По ООП тут можно сделать класс CypherMachine у которого будут поля secret_alphabet и keyword и
#! методы encode(message), decode(message). Ну и любое число "закрытых" вспомогательных методов.

def encode(message, secret_alphabet, keyword):
    # clean
    #! очистка должна удалять все, что отсутвует в алфавите.
    message = message.replace(" ", "").lower()

    coords = "ADFGVX"
    #! с данными в таком виде будет неудобно работать... у тебя основная операция - это
    #! поиск по символу алфавите, соответвенно тебе нужна мапа из символа алфавита в
    #! в пару из ADFGVX

    #! encoding_map = {}
    #! for i in range(len(secret_alphabet)):
    #!    y = i // len(coords)
    #!    x = i % len(coords)
    #!    encoding_map[secret_alphabet[i]] = coords[y] + coords[x] # или coords[x] + coords[y] я не помню правильный порядок
    #! так искать нужнуб букву буде прощее... encoding_map[letter]

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
    coo = "".join(coo)
    print((coo))

    # encode
    #! тут было бы проще порезать результат "координатных пар" из первого шага на строки длинной в
    #! наше секретное слово... а потом транспонировать получившийся результат и отсортировать.

    #! или опять же пользовать наш любимый остаток от деления и получить сразу нужные столбцы
    #! columns = {x: [] for x in clean_keyword}
    #! for offset, char in enumerate(flat_public_pairs):
    #!    i = offset % len(clean_keyword)
    #!    columns[clean_keyword[i]].append(char)
    #! потом сортируем и далее по инструкции

    # ! Ты тут как-то рано сортируешь секретное слово, по доке его нажно сортировать вместе со столбцами
    # ! которых у тебя еще нет.

    keyword = "".join(sorted(set(keyword), key=keyword.index))
    print(keyword)

    res = [coo[i : i + len(keyword)] for i in range(0, len(coo), len(keyword))]
    print("res", res)

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

    sorteddic = sorted(dic.keys())
    print(str(sorteddic))
    out = ""
    for i in sorteddic:
        out += dic[i]
    print(out)
    return out


def decode(message, secret_alphabet, keyword):
    return message


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"

    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"

    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"

    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"

    # assert decode("FXGAFVXXAXDDDXGA",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'iamgoing', "decode I am going"
    # assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'attackat1200am', "decode attack"
    # assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    # assert decode("DXGAXAAXXVDDFGFX",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'iamgoing', "decode weasel == weasl"
