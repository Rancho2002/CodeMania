def printNosRecur(x: int,arr:list=[]) -> list[int]: 
    # Write your code here
    if x==0:
        return

    printNosRecur(x-1,arr) 
    arr.append(x)


def printNos(x: int) -> list[int]:
    arr=[]
    printNosRecur(x,arr)
    return arr

print(printNos(5))

