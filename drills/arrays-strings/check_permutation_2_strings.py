class Solution:

    # time O(N log N) because of sort
    # space O(1) I think
    def permutation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return self.sort(s1) == self.sort(s2)

    def sort(self, string):
        return "".join(sorted(string))




    # time O(N)
    # space O(1)
    def permutationBetterComplexity(self, s1, s2):
        if len(s1) != len(s2):
            return False  # 0, 1, 2, 3,            127
        # considering strings are composed of the ASCII character alphabet letters = [0, 0, 0, 0, ........... 0]

        letters = [0] * 128

        for i in s1:
            letters[ord(i)] += 1

        for i in s2:
            letters[ord(i)] -= 1
            if letters[ord(i)] < 0:
                return False
        return True
