def printPattern(n):

    #Write your code here
    space=n-1
    pattern=0
    for k in range(n):
        for i in range(space,0,-1):
            print(" ",end="")
        for j in range(2*pattern + 1):
            print("*",end="")

        pattern+=1
        space-=1
        print()

printPattern(4)