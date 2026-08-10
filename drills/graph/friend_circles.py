class Solution:
    def findCircleNum(self, isConnected) -> int:

        num_provinces = 0
        visited = set()
        for city in range(len(isConnected)):
            if city not in visited:
                num_provinces += 1
                self._dfs(isConnected, city, visited)

        return num_provinces


    def _dfs(self, isConnected, city, visited):

        if city in visited:
            return

        visited.add(city)

        for neighbor in range(len(isConnected[city])):
            if isConnected[city][neighbor]:
                self._dfs(isConnected, neighbor, visited)


import unittest

class TestSolution(unittest.TestCase):
    sol = Solution()

    friends_list_1 = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]

    friends_list_2 = [[1, 1, 0, 0],
               [1, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    def test_friends_list_1(self):
        self.assertEqual(2, self.sol.findCircleNum(self.friends_list_1), 'should be 2')

    def test_friends_list_2(self):
        self.assertEqual(3, self.sol.findCircleNum(self.friends_list_2), 'should be 3')
        # sol.findCircleNum(friends)












