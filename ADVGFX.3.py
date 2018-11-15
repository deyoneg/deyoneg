def encode(message="I am going",
           secret_alphabet="dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
           keyword="cipher",
           debug=False):

    if debug:
        print("\n----------------\nCoding")
        print("Message :", message)


    # Our message is "I am going".
    # First we must clean and process the message: "iamgoing".
    # It should contain only digits and latin letters in lowercase.
    # All other characters (such as punctuation) are skipped. 
    message0 = ''.join(filter(lambda x:x.isalnum(), message.lower()))

    if debug:
        print("Cleaned message :", message0)


    # Then we fill the "adfgvx" table with our secret alphabet
    # "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g".
    indexes = "ADFGVX"
    adfgvx_table = [[secret_alphabet[6*i+j] for j in range(6)] for i in range(6)]

    if debug:
        print("ADFGVX table :")
        print("\n".join(
            ('\\  ' + ' '.join(indexes),
             ' \\' + '--'*len(indexes) ) +
            tuple(" ".join([indexes[i]+'|']+row) for i,row in enumerate(adfgvx_table))))
              

    # Using this square, the message is converted to fractionated form (row-column): 
    message1 = ''
    for x in message0:
        i, j = 0, 0
        while True:
            if x == adfgvx_table[i][j]:
                break
            j = (j + 1) % len(adfgvx_table[i])
            if j == 0:
                i += 1
        message1 += indexes[i] + indexes[j]

    if debug:
        print("Fractionated form :", ' '.join(message1[i:i+2] for i in range(0,len(message1),2)))


    # Then, a new table is created with a key as the heading.
    # Let's use 'cipher' as the key. If the key contains duplicated letters,
    # the first one should be used. So, "checkio" becomes "chekio". 
    keyword = ''.join(sorted(set(keyword), key=lambda x:keyword.index(x)))
    if debug:
        print("No duplicate in keyword :", keyword)
    
    nb_col = len(keyword)
    nb_row = (len(message1)-1)//nb_col + 1
    table1 = [[message1[nb_col*i+j] if nb_col*i+j < len(message1) else ''
             for j in range(nb_col)]
                 for i in range(nb_row)]
    if debug:
        print("Table 1 :")
        
        print('\n'.join((' '.join(keyword),'-'.join('-'*nb_col)) +
                        tuple(' '.join(row) for row in table1)))


    # The columns are sorted alphabetically based on the keyword
    # and the table changes to the new form. 
    sorted_kw = ''.join(sorted(keyword))

    if debug:
        print("Sorted keyword :", sorted_kw)
    

    table2 = [[row[keyword.index(sorted_kw[c])]
                for c in range(nb_col)]
                    for row in table1]

    if debug:
        print("Table 2 :")
        print('\n'.join((' '.join(sorted_kw),'-'.join('-'*nb_col)) +
                        tuple(' '.join((row[i] or ' ')
                                            for i in range(nb_col))
                                               for row in table2)))


    # Then it is read off in columns, in keyword order
    # and the result is "FXGAFVXXAXDDDXGA".
    message2 = ''.join(table2[i][j]
                       for j in range(nb_col)
                           for i in range(nb_row))

    if debug:
        print("Returned message :", message2)


    return message2




def decode(message="FXGAFVXXAXDDDXGA",
           secret_alphabet="dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
           keyword="cipher",
           debug=False):

    if debug:
        print("\n----------------\nDecoding")
        print("Message :", message)


    # first no duplicate in keyword
    keyword = ''.join(sorted(set(keyword), key=lambda x:keyword.index(x)))

    if debug:
        print("No duplicate in keyword :", keyword)
    

    # then compute directly the table1... no proud of that code
    sorted_kw = ''.join(sorted(keyword))

    if debug:
        print("Sorted keyword :", sorted_kw)
    
    nb_col = len(keyword)
    nb_row = (len(message)-1)//nb_col + 1

    table1 = [[""]*nb_col for _ in range(nb_row)]
    i = 0
    for col in range(nb_col):
        for row in range(nb_row):
            # compute the final col for no sorted keyword
            col2 = keyword.index(sorted_kw[col])
            # if the final place is blank
            if row * nb_col + col2 >= len(message):
                continue
            else: #place the letter
                table1[row][col2]=message[i] 
                i += 1

    if debug:
        print("Table 1 :")
        
        print('\n'.join((' '.join(keyword),'-'.join('-'*nb_col)) +
                        tuple(' '.join(row) for row in table1)))


    # read the table1 to get the fractionned form
    message1 = ''.join(''.join(row) for row in table1)

    if debug:
        print("Fractionated form :", ' '.join(message1[i:i+2] for i in range(0,len(message1),2)))


    
    # finally, get the decrypted message
    indexes = "ADFGVX"
    adfgvx_table = [[secret_alphabet[6*i+j] for j in range(6)] for i in range(6)]

    if debug:
        print("ADFGVX table :")
        print("\n".join(
            ('\\  ' + ' '.join(indexes),
             ' \\' + '--'*len(indexes) ) +
            tuple(" ".join([indexes[i]+'|']+row) for i,row in enumerate(adfgvx_table))))

    message0 = ''.join(adfgvx_table[indexes.index(message1[i])]
                                   [indexes.index(message1[i+1])] 
                     for i in range(0,len(message1),2) )
        
    if debug:
        print("Returned message :", message0)


    return message0


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"