class Solution:
    def rotate(self, nums, k) -> None:
        
        n = len(nums)
        
        k = k % n
        
        self.rotate_helper(nums, 0, n - 1)
        self.rotate_helper(nums, 0, k - 1)
        self.rotate_helper(nums, k, n - 1)

        
    def rotate_helper(self, nums, start, end):

        begin = start

        final = end

        while begin < final:
            nums[begin], nums[final] = nums[final], nums[begin]
            begin += 1
            final -= 1
