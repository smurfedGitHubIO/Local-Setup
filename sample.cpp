#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll n, m;
    cin >> n >> m;
    if(n == m<<1 || m == n<<1 || (max(n, m) - min(n,m) < min(n,m) && (n+m)%3 == 0))
        cout << "YES\n";
    else
        cout << "NO\n";
    return 0;
}