class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        min_sum =0
        m_stack =[]
        for i in range(len(arr)):
            while m_stack and m_stack[-1][1] > arr[i]:
                j,m = m_stack.pop()
                if m_stack:
                    left = j - m_stack[-1][0]
                else:
                    left = j +1
                right = i -j
                min_sum = (min_sum + left*right*m)%(10**9 +7)
            m_stack.append((i,arr[i]))
        return min_sum
                    

            