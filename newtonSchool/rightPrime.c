// # Your code here
// x=int(input())
// flag=False
// while(True):
//     for i in range(2,x):
//         print("Checking for",i)
//         if(x%i==0):
//             flag=True
//             break
    
//     if(flag):
//         x+=1
//         i=2
// # else:
// #     break
// print(x)
#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int flag=0;
    while(1){
        for(int i=2;i<n;i++){
            if(n%i==0){
                flag=1;
                break;
            }
        }
        if(flag==1){
            n++;
            flag=0;
        }
        else{
            break;
        }
    }
    printf("%d",n);
    return 0;
}