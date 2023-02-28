//https://www.codechef.com/submit/AGELIMIT
#include <stdio.h>

int main(void) {
	// your code goes here
	int total,req,pre,upp;
	scanf("%d",&total);
	for(int i=0;i<total;i++){
	    scanf("%d%d%d",&req,&upp,&pre);
	    if(pre>=req && pre<upp){
	        printf("YES\n");
	    }
	    else{
	        printf("NO\n");
	    }
	}
	return 0;
}


