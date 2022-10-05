# https://www.codechef.com/submit/PROGLANG
a=int(input())
for i in range(a):
    l=list(map(int,input().split()))
    # print(l)
    if((l[0]==l[2] and l[1]==l[3]) or (l[0]==l[3] and l[1]==l[2])):
        print(1)
    elif((l[0]==l[4] and l[1]==l[5]) or (l[0]==l[5] and l[1]==l[4])):
        print(2)
    else:
        print(0)
    l=[]