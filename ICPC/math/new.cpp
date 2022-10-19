#include <bits/stdc++.h>
using namespace std;
 
int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

 long long numOfDiv(int num) {
    int cnt = 0;
    for(int i=1;i*i<=num;i++) {
        if(num%i == 0) {
            if(num/i == i)
                cnt++;
            else
                cnt += 2;
        }
    }
    return cnt;
}


 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
   int t;
   cin>>t;
   long long x,y,gc=0;
   while (t--){
    cin>>x>>y;
    gc=gcd(x,y);
    cout<<numOfDiv(gc)<<"\n";

   }
    return 0;
}