class Solution:

    # time - O(n) where n is len(nums1)
    # space - O(1)

    def merge_new(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1



    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index2 = len(nums2) - 1
        index1 = len(nums1) - len(nums2) - 1
        
        i = len(nums1) - 1
        
        while index1 >=0 and index2 >= 0:
            
            if nums2[index2] >= nums1[index1]:
                
                nums1[i] = nums2[index2]
                index2 -= 1
                
            else:
                
                nums1[i] = nums1[index1]
                index1 -= 1
                
            i -= 1

        
        if index1 >= index2:
            
            for j in range(index1, -1, -1):
                nums1[i] = nums1[j]
                
                i -= 1
                
        else:
            
            for j in range(index2, -1, -1):
                nums1[i] = nums2[j]
                
                i-=1
                

    '''
        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        Output: [1,2,2,3,5,6]
    '''

# ======================================================================================================================
import unittest
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.bst = BST(10)
        self.bst.insert(5)

    def test_bst_preorder(self):
        self.assertEqual(self.bst.pre_order_traversal(), [10, 5, 2, 7, 15, 12, 30],
                         "test_bst_preorder root ---> left ---> right failed")

    def test_bst_inorder(self):
        self.assertEqual(self.bst.inOrderTraversal(), [2, 5, 7, 10, 12, 15, 30],
                         "test_bst_inorder left ---> root ---> right failed")


if __name__ == "__main__":
    unittest.main()



s = Solution()

            
nums1 = [1,2,3,0,0,0]

print(nums1)

m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)

print(nums1)
