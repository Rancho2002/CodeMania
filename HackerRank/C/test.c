#include <stdio.h>
int main() {
// int x=19, y=23;
// int j=(x++,--y);
// y+=3;
// printf("%d", j+y);

int x = -5, y = 8;

x = x + y - (y = x);  

printf("%d", x * y);

// printf("%f",10>>4);
return 0;
}