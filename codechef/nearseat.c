// https://www.codechef.com/submit/NEARESTEXIT
#include <stdio.h>

int main(void) {
	// your code goes here
	int total,a;
	scanf("%d",&total);
	for(int i=0;i<total;i++){
	    scanf("%d",&a);
	    if(a>50){
	        printf("RIGHT\n");
	    }
	    else{
	        printf("LEFT\n");
	    }
	}
	return 0;
}

