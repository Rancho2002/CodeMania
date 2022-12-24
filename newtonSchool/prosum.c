#include <stdio.h>
#include <math.h>
int main(){

    int n;
    int mod=pow(10,9)+7;
    scanf("%d",&n);
    int arr[n];
    unsigned long int ans=0;
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int sum=arr[n-1];
    for(int i=n-2;i<=0;i--){
        ans+=(ans+(sum*arr[i]));
        sum=sum+arr[i];

    }
    printf("%d",ans%mod);
    return 0;
}