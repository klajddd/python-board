class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) < 1 or len(nums2) < 1:
            return []

        result = []

        nums1.sort()
        nums2.sort()

        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):

            if nums1[i1] == nums2[i2]:

                if len(result) < 1:
                    result.append(nums1[i1])

                else:
                    if nums1[i1] != result[-1]:
                        result.append(nums1[i1])

                i2 += 1
                i1 += 1


            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                i1 += 1

        return result
