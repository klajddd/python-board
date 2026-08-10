class Solution:

    def findCircleNum(self, isConnected) -> int:

        def dfs(start):
            is_visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in is_visited:
                    dfs(end)

        is_visited = set()
        province_count = 0

        for start in range(len(isConnected)):
            if start not in is_visited:
                province_count += 1
                dfs(start)

        return province_count

if __name__=='__main__':
    s = Solution()
    # s.outer_func()
    isConnected = [[1,0,0,1],
                   [0,1,1,0],
                   [0,1,1,1],
                   [1,0,1,1]]
    print(s.findCircleNum(isConnected))

