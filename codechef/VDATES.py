# https://www.codechef.com/problems/VDATES
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a>=b and a<=c):
        print("Take second dose now")
    elif(a<b):
        print("Too Early")
    else:
        print("Too Late")