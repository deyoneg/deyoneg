VOWELS = "aeiouy"

def translate(phrase):
    import re
    phrase = re.sub(r"([^a^e^i^o^u^y^\s])[aeiouy]", r'\1', phrase)
    phrase = re.sub(r"([aeiouy])\1{2}", r'\1', phrase)
    print (phrase)
    return phrase

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
