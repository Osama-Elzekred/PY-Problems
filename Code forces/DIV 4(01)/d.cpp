/** أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ **/
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
#define o_0 cin.tie(0),ios::sync_with_stdio(0),cout.tie();
#define all(a) a.begin(),a.end()
#define allr(v) v.rbegin(), v.rend()
#define T  int t; cin >> t;while (t--)
#define lcm(x, y) x / __gcd(x, y) * y
#define filein freopen("second_second_friend_input.txt", "r", stdin);
#define fileout freopen("second_second_friend_output.txt", "w", stdout);
#define ll long long
using namespace __gnu_pbds;
using namespace std;
template <class type1>
using ordered_multiset = tree <type1, null_type, less_equal <type1>, rb_tree_tag, tree_order_statistics_node_update>;
ll n,m,z,x,y,mx;
const int c5=3e5+9;
const int c3=3e3+9;
const int N=1e5+5;
const int mod = 1e9+7;
const int mod2 =998244353;
const double PI = 3.141592653589793238460;
int dx[]={-1,0,0,1,1,-1,1,-1};
int dy[]={0,1,-1,0,1,-1,-1,1};
 
int main()
{
    o_0
    T
    {
        cin>>n;
        string s;
        cin>>s;
        x=0;
        for(int i=0;i<n;i++)
            (s[i]=='L')?x+=i:x+=(n-i-1);
        y=n;int i=0,j=n-1;
        while(y)
        {
            if(s[i]=='L')
            {
                x-=i,x+=(n-i-1);
                cout<<x<<' ';
                y--;
            }
            if(s[j]=='R')
            {
                x-=(n-j-1),x+=j;
                cout<<x<<' ';
                y--;
            }
            i++,j--;
            if(i>=n/2)break;
        }
        while(y--)
            cout<<x<<' ';
        cout<<'\n';
    }
}