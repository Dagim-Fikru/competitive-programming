class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                q = deque([i])
                color[i] = 0

                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]
                            q.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False

        return True