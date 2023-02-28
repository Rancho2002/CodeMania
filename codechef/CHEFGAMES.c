// https://www.codechef.com/problems/CHEFGAMES
#include <stdio.h>

int main(void) {
// your code goes here
int total,a,b,c,d;
scanf("%d",&total);
for(int i=0;i<total;i++){
   scanf("%d%d%d%d",&a,&b,&c,&d);
   if(a==0 && b==0 && c==0 && d==0)
   printf("IN\n");
   else
   printf("OUT\n");
}
return 0;
}