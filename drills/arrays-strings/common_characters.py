# find the common characters in each string
# strings = ["abc", "bcd", "cbad"]


# time O(n * m) where m is the length of the longest string --- SLIGHTLY BETTER
# space O(m) where m is the longest space
def commonCharacters(strings):
    # Write your code here.
    shortest = float('inf')
    indexOfShortest = None
    for i, s in enumerate(strings):
        if len(s) < shortest:
            shortest = len(s)
            indexOfShortest = i
    shortest = set(strings[i])

    for s in strings:
        temp = set(s)  # O(m) space where m is the longest string
        for char in list(shortest):
            if char not in temp:
                shortest.remove(char)
    return list(shortest)

# ======================================================================================================================


# time O(n * m) where n = len(strings), m = length(each string)
# space O(c) where c = common chars
def commonCharacters(strings):
    # Write your code here.
    result = []
    counter = dict()

    for s in strings:
        for char in set(s):
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    for char in counter:
        if counter[char] == len(strings):
            result.append(char)

    return result


strings = ["abc", "bcd", "cbad"]
print(commonCharacters(strings))