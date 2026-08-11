# time O(n * m) where n is number of words, m is length of longest word
# space O(n * m)
def semordnilap(words):
    # Write your code here.
    wordsSet = set(words)
    semordnilapPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)
    return semordnilapPairs