# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    loc1=x1;
    loc2=x2;
    flag=False
    

    while(True):
        loc1=loc1+v1
        loc2=loc2+v2
        if(x1<x2 and v1>v2):
            # print("Calling 1")
            if(loc2==loc1):
                flag=True
                break
            elif(loc1>loc2):
                break
        elif(x2<x1 and v2>v1):
            # print("calling 2")
            if(loc2==loc1):
                flag=True
                break
            elif(loc2>loc1):
                break
        else:
            break 
         
    if(flag):
        return "YES"
    else:
        return "NO"
        