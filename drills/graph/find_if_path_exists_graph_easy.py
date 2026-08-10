
class Solution:

    # time O(E + V)
    def validPath_dfs(self, n: int, edges, from_v: int, to_v: int) -> bool:
        graph = {}
        for v1, v2 in edges:
            if v1 in graph:
                graph[v1].append(v2)
            else:
                graph[v1] = [v2]
            if v2 in graph:
                graph[v2].append(v1)
            else:
                graph[v2] = [v1]

        def dfs(node, end, seen):
            if node == end:
                return True

            if node in seen:
                return False

            seen.add(node)

            for n in graph[node]:
                if dfs(n, end, seen):
                    return True

            return False

        return dfs(from_v, to_v, set())


    # time O(E + V)
    def validPath_bfs(self, n: int, edges, source: int, destination: int) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        seen = {source}
        path = [source]

        while len(path) > 0:
            current = path.pop()
            if current == destination:
                return True

            for neighbor in graph[current]:
                if neighbor not in seen:
                    path.append(neighbor)
                    seen.add(neighbor)
        return False


s= Solution()
print(s.validPath_dfs(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 2))
print(s.validPath_bfs(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 2))

