// https://www.codechef.com/submit/BIRYANI

#include <stdio.h>

int main(void) {
	// your code goes here
	int total;
	int per, course,result;
	scanf("%d",&total);
	for(int i=0;i<total;i++){
	    scanf("%d%d",&per,&course);
	    result=per*course;
	    printf("%d\n",result);
	}
	return 0;
}

