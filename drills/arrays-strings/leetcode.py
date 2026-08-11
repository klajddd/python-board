import math

def minEatingSpeed(piles, h):

    low = 1
    high = max(piles)
    res = high
    while high > low:
        hours = 0
        for p in piles:
            hours += math.ceil(p / high)
        if hours <= h:
            res = high
            hours = 0
            high -= 1
        else:
            break
    return res


# piles = [3,6,7,11]
# h = 8
# piles = [30,11,23,4,20]
# h = 5
piles = [30,11,23,4,20]
h = 6

print(minEatingSpeed(piles, h))