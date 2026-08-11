# time O(n)
# space O(n)
def zeroSumSubarray(nums):
    # Write your code here.
    sumSet = set([0])
    total = 0
    for el in nums:
        total += el
        if total in sumSet:
            return True
        else:
            sumSet.add(total)
    return False



#=======================================================================================================================


# time O(n^3)
# space O(1)
def zeroSumSubarray(nums):
    # Write your code here.
    result = False
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            run = False
            for k in range(i, j+1):
                if nums[k] is not None:
                    sum += nums[k]
                run = True
            if sum == 0 and run:
                result = True
                break
            run = False
    return result