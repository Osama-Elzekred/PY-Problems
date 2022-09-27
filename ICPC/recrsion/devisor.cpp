#include <bits/stdc++.h>
using namespace std;
#define FIO cin.tie(0), cin.sync_with_stdio(0);
#define siz(x) ((int)((x).size()))
typedef long long ll;
ll arr[10000001];
ll d(int n)
{
  int count=0;
  for(int i=1;i*i<=n;i++)
  {
    if(n/i == i && n%i==0)
      count ++;
    
    else if(n%i==0){count+=2;}
  }
  return count ;
}
int main()
{
  FIO 
  ll co=0;
  int a,b,c;
  cin>>a>>b>>c;
  // for ( int i = 1; i<=1000001; i++)
  // {
  //     arr[i]=d(i);
  // }
  
  for(int i=1;i<=a; i++)
  {
    for(int j=1;j<=b;j++)
    {
      for(int k=1;k<=c;k++)
      {
        if(arr[i*j*k] == 0)
          arr[i*j*k] = d(i*j*k);
        
        co+=arr[i*j*k];
      }
    }
  }
  
   cout<<co<<"\n";


  return 0;
}