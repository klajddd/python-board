
# time O(n+m)
# space O(c) -  where c is for characters
def generateDocument(characters, document):
    # Write your code here.
    from collections import defaultdict
    if document is "":
        return True
    char_freq = defaultdict(int)

    for el in characters:
        char_freq[el] += 1

    for el in document:
        if el not in char_freq:
            return False
        char_freq[el] -= 1
        if char_freq[el] < 0:
            return False
    return True

# ----------------------------------------------------------------------------------------------------------------------

# time O(m*(n+m))
# space O(1)
def generateDocument_shit(characters, document):
    # Write your code here.
    for char in document:
        documentFrequency = countCharacterFrequency(char, document)
        charactersFrequency = countCharacterFrequency(char, characters)
        if documentFrequency > charactersFrequency:
            return False
    return True



def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency

# ----------------------------------------------------------------------------------------------------------------------


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
3
import unittest
class TestGenerate(unittest.TestCase):

    def test_generate(self):
        self.assertEqual(generateDocument(characters, document), True, "Should be True")

