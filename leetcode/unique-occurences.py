class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arrN=list(set(arr))
        l=[]
        for i in range(len(arrN)):
            l.append(arr.count(arrN[i]))

        chk=set(l)

        if(len(chk)==len(l)):
            return True
        return False
# https://leetcode.com/problems/unique-number-of-occurrences/submissions/838936547/