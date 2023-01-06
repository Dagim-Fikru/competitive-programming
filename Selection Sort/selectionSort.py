#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        return self[i]
    def selectionSort(self, arr,n):
        #code here
        n=len(arr)
        for i in range(n):
            sml = i
            j=i+1
            while j<n:
                if arr[j]<arr[sml]:
                    sml=j
                j+=1
            if sml!=i:
                arr[i],arr[sml]=arr[sml],arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
