def migratoryBirds(arr):
    # Write your code here
    maxElem=0
    # arr_id=0
    # arr.sort()
    countelem=[]
    for i in range(5):
        countelem.append(arr.count(i+1))
    print(countelem)
    for i in range(5):
        if(maxElem<countelem[i]):
             maxElem=countelem[i]
             val=i+1
            #  arr_id=i+1
             
    return val

# l=[1,3,3,3,3,4]
l=[3,4,4,2,2,5,5,5]
print(migratoryBirds(l))