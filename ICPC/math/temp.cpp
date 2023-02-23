#include <bits/stdc++.h>
#define ll long long 
using namespace std;
vector<ll>primes;
void primefactor(ll m)
{

    //if(m<2){return primes;}
    for(ll i=2;i*i<=m;i++)
    {
        while(m%i==0)
        {
            primes.push_back(i);
            m/=i;
        }
    }
    if(m>1)
    {
        primes.push_back(m);
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll n;
    while(cin>>n)
    {
        if(n==0){break;}

        if(n<0)
        {
            n=n*(-1);
            primefactor(n);
            cout<<-1*n<<" = -1 x ";
            for(int i=0;i<primes.size();i++)
            {

                if(i==primes.size()-1)
                {
                    cout<<primes[i];
                }
                else
                {
                    cout<<primes[i]<<" x ";
                }
            }
            cout<<"\n";
        }
        else
        {
            primefactor(n);
            cout<<n<<" = ";
            for(int i=0;i<primes.size();i++)
            {
                if(i==primes.size()-1)
                {
                    cout<<primes[i];
                }
                else
                {
                    cout<<primes[i]<<" x ";
                }
            }
            cout<<"\n";
        }
        primes.clear();

    }
    return 0;
}