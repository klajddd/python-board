#  "AlgoExpert is the best!" ------> best! the is AlgoExpert

# time O(n)
# space O(n)
def reverseWords(self, s: str) -> str:
    result = s.split()
    
    n = len(result) - 1
    
    for i in range((n//2)+ 1):
        result[i], result[n - i] = result[n - i], result[i]
    
    return " ".join(result)


# =============================================================================
def reverseWordsInString(string):
    # Write your code here.
    if len(string) < 2:
        return string
    result = []
    start = -1
    space = 0

    for i in range(len(string)):
        if string[i] != ' ':
            if space != 0:
                result.append(' ' * space)
                space = 0
            if start == -1:
                start = i
        else:
            if start != -1:
                result.append(string[start:i])
                start = -1
            space += 1
    if space == 0:
        result.append(string[start:i + 1])
    else:
        result.append(' ' * space)

    return "".join(result[::-1])


print(reverseWordsInString("AlgoExpert is the best!"))