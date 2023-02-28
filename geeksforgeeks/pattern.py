# https://practice.geeksforgeeks.org/problems/triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_5

#User function Template for python3
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
class Solution:
    def printSquare(self, N):
        # Code here
        for i in range(N):
            for j in range(N):
                print("* ",end="")
            print()

'''
    *
   ***  
  *****
 *******
*********
'''
class Solution:
    def printTriangle(self, n):
        # Code here
        for i in range(n):
            for j in range(n-1,i,-1):
                print(" ",end="")
            for k in range(2*i+1):
                print("*",end="")
            print()

def pattern2(n):
    for i in range(n):
            for k in range(2*n-1,0,-1):
                print("*",end="")
            for j in range(n-1,i,-1):
                print(" ",end="")
            print()