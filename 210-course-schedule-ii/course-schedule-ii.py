class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        checked = [False] * numCourses
        stack = []
        for i in range(numCourses):
            path = [False] * numCourses
            if self.isCyclic(i, graph, stack, path, checked):
                return []

        res = [0] * numCourses
        for i in range(numCourses):
            res[i] = stack.pop()
        return res

    def isCyclic(self, node: int, graph: List[List[int]], stack: List[int], path: List[bool], checked: List[bool]) -> bool:
        if checked[node]:
            return False
        if path[node]:
            return True
        path[node] = True
        for adj in graph[node]:
            if self.isCyclic(adj, graph, stack, path, checked):
                return True
        stack.append(node)
        path[node] = False
        checked[node] = True
        return False
