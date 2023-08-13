class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        prev = 0
        curr = 1
        for i in range(2, n+1):
            prev, curr = curr, prev + curr
        
        return curr



a=Solution()
print(a.nthFibonacci(14521)) # 1 1 2 3 5 8