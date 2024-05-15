class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        adj=collections.defaultdict(list)
        
        for s,d in redEdges:
            adj[s].append([d,1])
        
        for s,d in blueEdges:
            adj[s].append([d,0])
        
        ans=[-1]*(n)
        ans[0]=0

        q=collections.deque()
        q.append([0,0,0])
        q.append([0,0,1])
        
        vis=[[0]*2 for _ in range(n)]

        while q:
            nd,nd_cst,last_flag = q.popleft()
            if ans[nd] ==-1 or ans[nd]>nd_cst:
                ans[nd]=nd_cst
            for nbr ,flag in adj[nd]:
                if vis[nbr][flag]:
                    continue
                else:
                    if flag==last_flag:
                        continue
                    vis[nbr][flag]=1
                    q.append([nbr,nd_cst+1,flag])
        return ans
                    