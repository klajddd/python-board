class Solution:

    # time O(n)
    # space O(n)
    def findKthPositive_n_time_n_space(self, arr, k):

        array_set = set(arr)

        for i in range(1, len(arr) + k + 1):
            if i not in array_set:
                k -= 1

            if k == 0:
                return i
            
    def findKthPositive_n_time_1_space(self, arr, k):

        # if the kth missing is less than x[0]
        if k <= arr[0] - 1:
            return k
        else:
            k = k - (arr[0] - 1)

        # search kth missing between the array numbers
        for i in range(len(arr) - 1):
            # missing between x[i] and x[i + 1]
            current_value = arr[i]
            next_value = arr[i + 1]
            missing_between_next_values = next_value - current_value - 1


            # if the kth missing is between x[i] and x[i + 1] -> return it
            if k <= missing_between_next_values:
                return current_value + k
            # otherwise, proceed further
            k -= missing_between_next_values

        # if the missing number if greater than x[-1]
        return arr[-1] + k


    def findKthPositive_logn_time_1_space(self, arr, k):

        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            # If number of missing integers before x[middle] < k ===> search on the right
            if arr[middle] - (middle + 1) < k:
                left = middle + 1

            else:
                right = middle - 1

        return left + k


