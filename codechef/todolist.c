#include <stdio.h>

int main(void) {
	// your code goes here
	int total, sp, count=0;
	scanf("%d",&total);
	for(int i=0; i<total;i++){
	    scanf("%d",&sp);
	    int arr[sp];
	    for(int j=0;j<sp;j++){
	        scanf("%d",&arr[j]);
	    }
	    for (int k=0;k<sp;k++){
	        if(arr[k]>=1000)
	            count++;
	    }
	    printf("%d\n",count);
	    count=0;
	}
	return 0;
}

