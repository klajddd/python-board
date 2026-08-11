# find first non-repeating char in string, return i
#  "abcdcaf" --- RESULT = 1


# time O(n)
# space O(1) - 26 chars in alphabet
def firstNonRepeatingCharacter(string):
    # Write your code here.
    char_frequencies = {}

    for char in string:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    for i in range(len(string)):
        if char_frequencies[string[i]] == 1:
            return i
    return -1


# ----------------------------------------------------------------------------------------------------------------------

# time O(n^2)
# space O(1)

def firstNonRepeatingCharacter(string):
    # Write your code here.

    for i in range(len(string)):
        foundDuplicate = False

        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                foundDuplicate = True
        if not foundDuplicate:
            return i
    return -1