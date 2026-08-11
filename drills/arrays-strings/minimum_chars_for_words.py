# "words": ["this", "that", "did", "deed", "them!", "a"]
# ["!", "a", "d", "d", "e", "e", "h", "i", "m", "s", "t", "t"]
# return the minimum amount of chars to form every word


# time O(n * w) - n is length of words array, w is length of longest word
# space O(c) where c is the length of characters of all words

def minimumCharactersForWords(words):
    # Write your code here.
    from collections import defaultdict
    char_total = defaultdict(int)
    char_word = defaultdict(int)
    result = []

    for word in words:
        for ch in word:
            char_word[ch] += 1
        for k, v in char_word.items():
            if char_total[k] < v:
                char_total[k] = v
        char_word = defaultdict(int)
    for k, v in char_total.items():
        for i in range(int(v)):
            result.append(k)

    return result