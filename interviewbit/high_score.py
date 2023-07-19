import math

class Solution:
    # @param A : list of list of strings
    # @return an integer
    def highestScore(self, A):
        mp={}

        for i in A:
            if i[0] in mp:
               mp[i[0]][0]+=int(i[1])
               mp[i[0]][1]+=1
            else:
                mp[i[0]]=[int(i[1]),1]
        
        l=[]
        
        for i in mp:
            l.append(math.floor(mp[i][0]/mp[i][1]))
        
        return max(l)

a=Solution()
print(a.highestScore([
  ["whkot", 61],
  ["nsk", 87],
  ["szygh", 69],
  ["nsk", 90],
  ["pxnh", 86],
  ["szygh", 22],
  ["wtct", 75],
  ["fsejl", 9],
  ["juqq", 88],
  ["gpmqr", 84],
  ["whkot", 18],
  ["nsk", 0]
]))