def sort(arr:list)->None:
        i=0
        j=0
        k=len(arr)-1
        
        while j<=k:
            if arr[j]==2:
                arr[j],arr[k]=arr[k],arr[j]
                k-=1
                
            elif arr[j]==1:
                j+=1
            
            elif arr[j]==0:
                arr[j],arr[i]=arr[i],arr[j]
                j+=1
                i+=1

# arr=[1 ,2, 2, 1, 2, 0, 2, 2]
arr=[2, 2, 1, 2,1]
sort(arr)
print(arr)