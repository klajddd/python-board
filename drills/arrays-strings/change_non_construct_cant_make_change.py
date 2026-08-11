# time O(nlog(n))
# space O(1)
def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0

    for coin in coins:
        if coin > currentChangeCreated +1:
            return currentChangeCreated+1

        currentChangeCreated += coin
    return currentChangeCreated + 1



# ----------------------------------------------------------------------------------------------------------------------
def subsetss(nums):
    def backtrack(first=0, curr=[]):
        if len(curr) == k: # if the combination is done
            output.append(curr[:])
            return
        for i in range(first, n):
            curr.append(nums[i]) # add nums[i] into the current combination
            backtrack(i + 1, curr) # use next integers to complete the combination
            curr.pop() # backtrack

    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output


def nonConstructibleChange_2(coins):

    all = set(coins)

    subs = subsetss(coins)
    for el in subs:
        if len(el)>0:
            all.add(sum(el))

    result = 1
    while result in all:
        result += 1

    return result
# ----------------------------------------------------------------------------------------------------------------------

coins = [5, 7, 1, 1, 2, 3, 22]
assert nonConstructibleChange(coins) == 20
