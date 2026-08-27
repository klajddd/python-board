def diffWaysToCompute(self, input):
    if input.isdigit():
        return [int(input)]
    result = []
    
    for i in range(len(input)):
        if input[i] in "-+*":
            result1 = self.diffWaysToCompute(input[:i])
            result2 = self.diffWaysToCompute(input[i+1:])
            for j in result1:
                for k in result2:
                    result.append(self.helper(j, k, input[i]))
    return result
      

def helper(self, j, k, operation):
    if operation == "+":
        return j+k
    elif operation == "-":
        return j-k
    else:
        return j*k


"""
    def diffWaysToCompute(self, input, memo={}):
        # :type input: str
        # :rtype: List[int]
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input] 
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
"""
