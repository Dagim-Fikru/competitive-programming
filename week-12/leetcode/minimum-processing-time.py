class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(tasks)
        processorTime.sort()
        tasks.sort(reverse=True)
        ans=0
        taskIndex = 0
        for i in processorTime:
            currMax = 0
            one_task= 0
            while taskIndex<n and one_task<4:
                currMax = max(currMax,tasks[taskIndex]+i)
                taskIndex+=1
                one_task+=1
            ans = max(ans,currMax)
        return ans








