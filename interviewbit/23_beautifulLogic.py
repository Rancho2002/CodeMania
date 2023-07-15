class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if not A:  # Check for empty string
            return 0
        
        A = A.strip()  # Strip leading and trailing spaces
        if A == "":
            return 0
        
        l = A.split()
        return len(l[-1])
