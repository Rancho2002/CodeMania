#include <stdio.h>

int main(){
    int a,count,limit;
    scanf("%d",&a);
    for(int i=0;i<a;i++){
        count=0;
        scanf("%d",&limit);
        for(int i=0;i<limit;i++){
            for(int j=0;j<limit;j++){
                if((i+j)%2!=0){
                    count++;
                }
            }
        }
        printf("%d\n",count);
    }
    return 0;
}