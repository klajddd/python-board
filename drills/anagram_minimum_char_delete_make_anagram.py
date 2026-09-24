# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
'''
Given two strings,  and , that may or may not be of the same length, determine the minimum number of character
deletions required to make  and  anagrams.
Any characters can be deleted from either of the strings.
Example
Delete  from  and  from  so that the remaining strings are  and  which are anagrams. This takes  character deletions.
'''
from collections import defaultdict


def makeAnagram(a, b):
    ans = 0

    d = defaultdict(int)

    for el in a:
        d[el] += 1

    for el in b:
        d[el] -= 1

    for el in d.keys():
        ans += abs(d[el])

    return ans


if __name__ == '__main__':
    a = input('enter first string')
    b = input('enter second string')
    res = makeAnagram(a, b)
    print(res)