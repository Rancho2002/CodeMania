a,b=map(int,input().split())
arr=list(map(int,input().split()))
if(a==1):
    print(arr[0])
    exit
h,l,test=b-1,0,[]
while(h<a): # (number of ballon to burst-1) is less than have ballons
    s=arr[h]-arr[l]
    if(arr[h]<0 and arr[l]<0): s+=abs(arr[h])
    elif(arr[l]>arr[h]): s+=abs(arr[h])
    else: s+=abs(arr[l])
    test.append(s)
    h+=1
    l+=1
print(min(test))