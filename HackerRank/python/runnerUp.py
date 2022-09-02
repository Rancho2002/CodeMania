if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxVal=arr[0]
    max2=arr[0]
    for i in range(len(arr)):
        if(maxVal<arr[i]):
            max2=maxVal
            maxVal=arr[i]
    print(max2)