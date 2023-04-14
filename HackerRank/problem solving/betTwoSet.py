def check(arr:list,key)->bool:
    for i in arr:
        if key%i==0 or i%key==0:
            continue
        else:
            # print("False ",key,i)
            return False
    # print("True",key)
    return True

def getTotalX(a, b):
    f1=set()
    f2=set()
    
    for i in range(2,max(min(a),min(b))+1):
        
        if(check(a,i)):
            f1.add(i)
            # print("f1",f1)
            
        if(check(b,i)):
            f2.add(i)

            
        f1=f1.intersection(f2)
    return len(f1)


print(getTotalX([3,9,6],[36,72]))

# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true