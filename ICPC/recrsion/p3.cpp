#include <bits/stdc++.h>
using namespace std;
#define FIO cin.tie(0), cin.sync_with_stdio(0)
#define siz(x) ((int)((x).size()))
typedef long long ll;
// ll i = n-1
ll rec(ll n,int i)
{
  if(n==1||n==2){return 1;}
  
  
  return i*rec(n-1,--i);
  
}
int main()
{
  ll n;
  cin>>n;
  cout<<rec(n,n)<<"\n";
  return 0;
}