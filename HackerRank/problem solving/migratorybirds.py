def migratoryBirds(arr):
    # Write your code here
    maxElem=0
    arr.sort()
    for i in range(len(arr)):
        countelem=arr.count(arr[i])
        if(maxElem<countelem):
             maxElem=countelem
             val=arr[i]
    return val

# l=[1,3,3,3,4]
l=[3,4,4,2,2,5]
print(migratoryBirds(l))