# time O(n)
# space O(1)
def bestSeat(seats):
    # Write your code here.
    bestSeat = -1
    currentMaxSpace = 0
    maxSpace = 0
    trailingPointer = 0
    leadingPointer = 1

    while leadingPointer < len(seats):

        if seats[leadingPointer] == 1:
            maxSpace = leadingPointer - trailingPointer

            if maxSpace > 1:
                if maxSpace > currentMaxSpace:
                    bestSeat = (maxSpace // 2) + trailingPointer
                    currentMaxSpace = maxSpace

            trailingPointer = leadingPointer

        leadingPointer += 1

    return bestSeat

#   "seats": [1, 0, 1, 0, 0, 0, 1]
#                         ^
# result = 4