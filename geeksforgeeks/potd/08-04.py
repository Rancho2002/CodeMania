def same(n:int,m:int)->bool:
    if(n>=0 and m>=0) or (n<=0 and m<=0):
        return True
    return False
    
class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        # points=set()
        # for i in range(1,len(arr)-1):
        #     # print(i)
        #     if(same(arr[i],arr[i+1])):
        #         points.add(arr[i])
        #         points.add(arr[i+1])

        # return list(points)

        n=len(arr)
        i=0
        while(i<n):
            if(not same(arr[i],arr[i+1])):
                print(arr[i],arr[i+1])
                arr.remove(arr[i])
                arr.remove(arr[i])

            n=len(arr)
            i+=1

        return arr
n=Solution
arr=[2, 1, -4, 3, -5, 2, 6, -3]
# arr=[4,2,-2,1]

print(n.makeBeautiful(8,arr))



'''
class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            res.append(arr[i])
        i = 0
        while i < len(res):
            if i+1 < len(res):
                if (res[i] >= 0 and res[i+1] < 0) or (res[i] < 0 and res[i+1] >= 0):
                    res.pop(i)
                    res.pop(i)
                    if i != 0:
                        i -= 1
                else:
                    i += 1
            else:
                i += 1
        return res

'''