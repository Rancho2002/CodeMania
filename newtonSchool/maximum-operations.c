#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library


int main() {
	// Your code here
    int n,flag=1,count=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++) scanf("%d",&arr[i]);
    while(flag==1){
        for(int i=0;i<n;i++){
            if(arr[i]%2==0) {
                arr[i]=arr[i]/2;
                count++;
            }
            else {
                flag=0;
                break;
            }
        }
    }
    printf("%d",count/n);
    return 0;
}