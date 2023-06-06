class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []
        for i in range(len(A)):
            if A[i] == "(" or A[i] == "{" or A[i] == "[":
                stack.append(A[i])
            elif len(stack) > 0:
                if A[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif A[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif A[i] == "]" and stack[-1] == "[":
                    stack.pop()
            else:
                return 0
        if not stack:
            return 1
        return 0


a = Solution()
print(a.isValid("((((([{()}[]]]{{{[]}}})))))"))
