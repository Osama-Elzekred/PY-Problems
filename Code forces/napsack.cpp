#include <bits/stdc++.h>

using namespace std;
#define FIO cin.tie(0), cin.sync_with_stdio(0)
#define siz(x) ((int)((x).size()))
typedef long long ll;
 int  n ;
int maxw; 
int arrw[5];
int arrv[5];
  ll f(ll w,ll v,ll p)
{
  
  if(w+arrw[p]>maxw||p>=n){return v;}
  
  // maxv+=v;
  // priority_queue<ll>pq;
  v=max(f(w,v,p+1), f(w+arrw[p], v+arrv[p] ,p+1));
  return v;

}
ll solve(){

  cin>>n>>maxw;
  for(int i=0;i<n;i++){
   cin>>arrv[i]>>arrw[i];
   
  }
  
// ll maxv;



return f(0,0,0);
}



int main(int argc, char **argv){

  cout<<solve()<<endl;

}