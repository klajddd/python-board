'''
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

'''

class Solution:


    '''
    Time Complexity: O(maxK ^countK * n)
    where \text{maxK}maxK is the maximum value of kk, \text{countK}countK is the count of nested kk probabilities and nn is the maximum length of encoded string. Example, for s = 20[a10[bc]], \text{maxK}maxK is 2020, \text{countK}countK is 22 as there are 22 nested kk probabilities (20 and 10) . Also, there are 22 encoded strings a and bc with maximum length of encoded string ,nn as 22


    Space Complexity: \mathcal{O}(\text{sum}(\text{maxK} ^ {\text{countK}}\cdot n))O(sum(maxK
    countK
 ⋅n)), where \text{maxK}maxK is the maximum value of kk, \text{countK}countK is the count of nested kk probabilities and nn is the maximum length of encoded string.
    '''
    def decodeString_array_join_instead_of_string(self, s: str) -> str:

        stack = []
        current_str = []
        num = 0

        for el in s:

            if el.isdigit():
                num = num * 10 + int(el)

            elif el == '[':
                stack.append([''.join(current_str), num])
                num = 0
                current_str = []

            elif el == ']':
                prev_string, prev_num = stack.pop()
                current_str = [prev_string + ''.join(current_str) * prev_num]

            else:
                current_str.append(el)

        return ''.join(current_str)



    def decodeString(self, s: str) -> str:

        """
        When we hit an '[', we know we have parsed k for the contents of the bracket;
        Push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
        the enclosed string k times.
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:

            if char == "[":
                stack.append((current_string, k))
                current_string = ""
                k = 0

            elif char == "]":
                last_string, last_k = stack.pop(-1)
                current_string = last_string + last_k * current_string

            elif char.isdigit():
                k = k * 10 + int(char)

            else:
                current_string += char

        return current_string

if __name__=="__main__":
    assert Solution.decodeString(None, "3[a2[c]]") == "accaccacc"

