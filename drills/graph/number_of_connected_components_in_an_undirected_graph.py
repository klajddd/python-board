class Solution:
    def countComponents(self, n: int, edges) -> int:

        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)

        visited = [0] * n

        g = {x: [] for x in range(n)}

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        result = 0

        for i in range(n):
            if not visited[i]:
                dfs(i, g, visited)
                result += 1

        return result

# ==============================================================================================================
# ==============================================================================================================

    def countComponents_adjacency_matrix(self, n: int, edges: List[List[int]]) -> int:

        matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

        for x, y in edges:
            matrix[x][y] = 1
            matrix[y][x] = 1

        connections = 0

        visited = set()

        for start in range(n):
            if start not in visited:
                connections += 1
                self.dfs(matrix, start, visited)
        return connections

    def dfs(self, matrix, start, visited):

        if start in visited:
            return

        visited.add(start)

        for neighbor in range(len(matrix)):
            if matrix[start][neighbor]:
                self.dfs(matrix, neighbor, visited)