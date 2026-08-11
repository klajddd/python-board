from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        start = 0
        end = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
                result += 1

        while start < end:
            if nums[start] is None:
                if nums[end] is not None:
                    nums[end], nums[start] = nums[start], nums[end]
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1
        print(f'nums are {nums}')
        return result
    

l = [0,1,2,2,3,0,4,2]
val = 2
s = Solution()
print(s.removeElement(l, val))


'''
def removeElement(self, nums: List[int], val: int) -> int:

        i,j=0,len(nums)-1;
        if(j==-1): return 0
        while(i<j):
            if(nums[i]==val):
                while(i<j and nums[j]==val): 
                    j-=1
                nums[i]=nums[j];
                j-=1
                continue;
            i+=1
        return i+1 if nums[i]!=val else i

'''