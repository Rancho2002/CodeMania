class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, k):
        # code here
        ans = []
        s = 0
        while (s <= N):
            if (k < N):
                if (s <= k):
                    new = arr[s:s+k]
                    new.reverse()
                    for i in new:
                        ans.append(i)
                    rest = arr[s+k:s+k+k]
                    rest.reverse()
                    for i in rest:
                        ans.append(i)
                s = s+k
            else:
                ans = arr
                ans.reverse()
                arr[:] = list(ans)
                return
        if (len(ans) != len(arr)):
            rest = arr[-len(ans):]
            for i in rest:
                ans.append(i)
        arr[:]=list(ans)


a= Solution()
l=list(map(int,input().split()))
print(a.reverseInGroups(l,5,3))