#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;
 
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll t;
	cin >> t;
	while(t--){
		ll x, y;
		cin >> x >> y;
		if(y == x)
			cout << (x*x) - y + 1 << "\n";
		else if(y > x){
			if(y&1)
				cout << (y*y) - (x) + 1 << "\n";
			else
				cout << ((y-1)*(y-1)) + (x) << "\n";
		}
		else{
			if(!(x&1))
				cout << (x*x) - (y) + 1 << "\n";
			else
				cout << ((x-1)*(x-1)) + (y) << "\n";
		}
	}
	return 0;
}