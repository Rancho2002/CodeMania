#include <stdio.h>

int main(){
    unsigned long int sum=0;
    int a;
    scanf("%d",&a);
    int arr[a];
    for(int i=0;i<a;i++){
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<a-1;i++){
        for(int j=1;j<a;j++){
            if(i<j && i!=j)
            sum+=arr[i]*arr[j];
        }
    }
    printf("%ul",sum);
    return 0;
}