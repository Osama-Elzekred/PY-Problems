// #include <bits/stdc++.h>
// using namespace std;
// #define FIO cin.tie(0), cin.sync_with_stdio(0)
// #define siz(x) ((int)((x).size()))
// typedef long long ll;
// // ll i = n-1

// int main()
// {
//   string s;cin>>s;
//   sort(s.begin(),s.end());
//   reverse(s.begin(),s.end());
//   char c =s[0];
//   for(int i=0;i<s.size();i++)
//   {
//     if(s[i]==c)cout<<s[i];
//   }
//   return 0;
// }
#include <cstdio>
#include <iostream>
using namespace std;

int tapeLen, n, trackLen[20];
int ans, nearestTotal;

void choose(int total, int mask, int p) {
	if (total > tapeLen)
		return;
	if (total > nearestTotal) {
		nearestTotal = total;
		ans = mask;
	}
	if (p >= n)
		return;

	choose(total + trackLen[p], mask | (1 << p), p + 1);
	choose(total, mask, p + 1);
}

int main() {
	while (scanf("%d %d", &tapeLen, &n) != EOF) {
		for (int i = 0; i < n; i++) {
			scanf("%d", &trackLen[i]);
		}

		ans = -1;
		nearestTotal = -1;
		choose(0, 0, 0);

		for (int i = 0; i < n; i++) {
			if ((ans >> i) % 2)
				printf("%d ", trackLen[i]);
		}
		printf("sum:%d\n", nearestTotal);
	}

	return 0;
}