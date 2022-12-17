#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double h, s;
    cin >> h >> s;
    double ans = h / s;
    printf("%.5f",ans);
    return 0;
}