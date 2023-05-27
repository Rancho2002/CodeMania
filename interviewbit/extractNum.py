import re
class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        variable=map(int,re.findall("\d+",A))
        return sum(variable)