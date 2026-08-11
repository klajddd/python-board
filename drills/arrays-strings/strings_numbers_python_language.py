class Solution:
    def reverseString(self, s):
        chars = list(s)
        for i in range(len(s) // 2):
            temp = chars[i]
            chars[i] = chars[len(s)-1-i]
            chars[len(s)-1-i] = temp
        return ''.join(chars)

    def is_palindrome(self, s):
        chars = list(s)
        for i in range(len(s) // 2):
            if chars[i] != chars[len(chars)-1-i]:
                return False
        return True

    def lowerCaseLetterWithIndex(self, str, index):
        if index < 0 or index > len(str)-1:
            raise IndexError("Index out of range")
        res = str[0:index] + str[index:index+1].lower() + str[index+1:]
        return res

    def convertToBinary(self, num):
        return bin(num)

    def manuallyConvertToBinary(self, num):
        binaryNum = [0] * num
        i = 0
        while num > 0:
            binaryNum[i] = num % 2
            num = int(num / 2)
            i += 1
        res = ''
        for i in binaryNum[::-1]:
            res += str(i)
        return res

    def addBinary(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1], b[0:-1])+'1'

    # Time O(N)
    # Space O(1)
    def isUnique(self, inputString):
        if len(inputString) > 128:  # ASCII alphabet made of 128 characters
            return False
        char_set = [False] * 128
        for i in inputString:
            if char_set[ord(i)]:  # return ASCII integer value of the character
                return False
            char_set[ord(i)] = True
        return True

    def permutation(self, s1, s2):
        if len(s1) != len(s2):
            return False 


s = Solution()
print(s.reverseString('klajd'))
print('palindrome: {}'.format(s.is_palindrome('aBaba')))
print('lower {}'.format(s.lowerCaseLetterWithIndex('KLAJD', 2)))
print('to binary {}'.format(s.convertToBinary(5)))
print('to binary manually {}'.format(s.manuallyConvertToBinary(5)))


# ==================== BUILT IN DATA STRUCTURES ====================
def dataStructures():

    dict = {'one': 1, 'two': 2, 'three': 3}

    dict.keys()


# ====================== EXCEPTIONS IN PYTHON ======================
def exception(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError as e:
        print('Invalid argument: {}'.format(e))
