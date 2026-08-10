from collections import UserList

class Solution:
    def findCenter(self, edges) -> int:

        center = None

        if len(edges) < 2:
            return None

        node1, node2 = edges[0]

        for el in edges[1:]:
            for node in el:
                if node == node1:
                    center = node1
                elif node == node2:
                    center = node2
            break
        return center



if __name__=='__main__':
    edges = [[1, 2], [2, 3], [4, 2]]
    s = Solution()
    print(s.findCenter(edges))

    edges2 = [[1, 2], [2, 3]]
    s = Solution()
    print(s.findCenter(edges))


'''
LINK: https://leetcode.com/problems/find-center-of-star-graph/


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
'''