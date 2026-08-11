'''

Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

'''

def find_unique(arr, k):
    
    result_arr = [0] * 32
    result = 0
    
    for num in arr:

        bin_num = bin(num)
        
        for i in range(len(bin_num[2:])):
            bit = num >> i # shift to check last bit at a time
            bit = bit & 1 # zero all other bits
            result_arr[i] += bit

    for i in range(32):
        result_arr[i] = result_arr[i] % k

    # x = [6, 1, 3, 3, 3, 6, 6]
    # then result_arr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, bit in enumerate(result_arr):
            result += bit * 2 ** i

    return result


arr = [6, 6, 110, 3, 3, 3, 3, 6, 6]
k = 4

print(find_unique(arr, k))

# import sys 

# INT_SIZE = sys.getsizeof(int) 

# print(INT_SIZE)








