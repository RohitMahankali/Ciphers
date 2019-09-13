from sys import argv


def main():
    cipher_text = argv[1]
    known_text = argv[2]
    f1 = open(cipher_text)
    f2 = open(known_text)
    cText = f1.read()
    kText = f2.read()
    cText = cText.lower()
    kText = kText.lower()
    kLetters = {
        " " : 0,
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0
    }
    cLetters = {
        " ": 0,
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    li1 = [] #For known text
    li2 = [] #For cipher text
    for char in kText:
        if char in kLetters:
            kLetters[char]+=1
    length_known = len(kText)
    for key in kLetters.keys():
        kLetters[key]/=(length_known*1.0)
    print kLetters

    for char in cText:
        if char in cLetters:
            cLetters[char]+=1
    length_cipher = len(cText)
    for key in cLetters.keys():
        cLetters[key]/=(length_cipher*1.0)
    print cLetters

    for key in kLetters.keys():
        li1.append(key)
        li1.sort(key=lambda k : kLetters[k])

    print li1
    li1Freq = []
    for item in li1:
        li1Freq.append(kLetters[item])

    print li1Freq

    for key in cLetters.keys():
        li2.append(key)
        li2.sort(key=lambda c : cLetters[c])

    print li2
    li2Freq = []
    for item in li2:
        li2Freq.append(cLetters[item])
    
    print li2Freq


    dText = ""

    for char in cText:
        if char not in li2:
            dText+=char
            continue
        elif char in li2:
            pos = li2.index(char)
            dText+=li1[pos]

    #print dText









if __name__ == "__main__":
    main()