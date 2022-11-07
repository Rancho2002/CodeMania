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


