# O(n) time
# O(n) space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    from string import ascii_lowercase as alph
    alph = alph + alph
    key = key % len(alph)
    n = len(string)
    result = []

    for el in string:
        index = alph.index(el)
        index = index + key
        el = alph[index]
        result.append(el)

    return ''.join(result)


# ----------------------------------------------------------------------------------------------------------------------

# O(n) time
# O(n) space

def caesarCipherEncryptor(string, key):
    from string import ascii_lowercase as alph
    newLetters = []
    newKey = key % 26
    alphabet = list(alph)
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)


def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.i(letter) + key
    return alphabet[newLetterCode % 26 ]
