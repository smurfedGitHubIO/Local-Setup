#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;
 
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll t;
	cin >> t;
	for(ll i=1; i<=t; i++){
		ll ns = i*i, n2 = (ns*(ns-1))/2;
		if(i > 2)
			n2 -= 4*(i-1)*(i-2);
		cout << n2 << "\n";
	}
	return 0;
}