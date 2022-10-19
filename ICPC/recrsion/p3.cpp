#include <bits/stdc++.h>
using namespace std;
 
int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}
 
int commDiv(int a, int b)
{
    int n = gcd(a, b);
 
    int result = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            if (n / i == i)
                result += 1;
            else
                result += 2;
        }
    }
    return result;
}
 
int main()
{
   int t;
   cin>>t;
   long long x,y,mx,mn;
   while (t--){
    cin>>x>>y;
    cout<<commDiv(x,y)<<endl;

   }
    return 0;
}