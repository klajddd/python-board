def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]

    gap = 0

    j = 0

    for i in range(len(binary)):

        if binary[i] == '1':
            gap = max(gap, i - j - 1)

            j = i

    return gap

print(solution(2147480640))