class Solution:
    def removeDuplicates(self, nums) -> int:
        total_dups = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = None
                total_dups += 1
        follower = 0
        leader = 1
        #         [1,1,2]

        for i in range(len(nums)):
            if leader < len(nums):
                c_follower = nums[follower]
                c_leader = nums[leader]
                if c_follower is None:
                    if c_leader is not None:
                        nums[follower] = c_leader
                        nums[leader] = c_follower
                        follower += 1
                else:
                    follower += 1
                leader += 1

        return len(nums) - total_dups



def delete_duplicates(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    print(A)
    return write_index


a = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print(delete_duplicates(a))
