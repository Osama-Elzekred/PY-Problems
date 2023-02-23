#include <bits/stdc++.h>
// #include<vector>
// #include<iostream>
using namespace std;
#define FIO cin.tie(0), cin.sync_with_stdio(0)
#define siz(x) ((int)((x).size()))
typedef long long ll;

ll a, b;

bool check(ll x){
    ll aa = a, bb = b;
    aa -= x;
    bb -= x;
    return aa >= 0 && bb >= 0 && aa+bb >= 2*x;
}
 
int BS(){
    ll l = 0, r = 2e9, mid;
 
    while(l < r){
        mid = l + (r-l+1) / 2;
        if(check(mid)){
            l = mid;
        }else{
            r = mid - 1;
        }
    }
 
    return l;
}
 
int main(){
    FIO;
    
    int t;
    cin >> t;
    while(t--){
        cin >> a >> b;
        cout << BS() <<"\n";
    }
 
    return 0;
}
 
 