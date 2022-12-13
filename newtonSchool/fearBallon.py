# https://my.newtonschool.co/playground/code/v0jkor49zn34
import sys
a,b=map(int,input().split())
arr=list(map(int,input().split()))
# print(arr)
if(a==1):
    print(abs(arr[0]))
else:
    h,l,ms=b-1,0,sys.maxsize
    while(h<a): # (number of ballon to burst-1) is less than have ballons
        s=arr[h]-arr[l]
        if(arr[h]<0 and arr[l]<0): s+=abs(arr[h])
        elif(abs(arr[l])>abs(arr[h])): s+=abs(arr[h])
        else: s+=abs(arr[l])
        ms=min(ms,s)
        l+=1
        h+=1
    print(ms)