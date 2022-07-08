#include <iostream>

using namespace std;
int n, ans = 0;
int row[15];

bool check(int j){
    for (int i = 0; i<j; i++){
        if(row[j] ==row[i] || abs(row[j] - row[i]) == abs(j-i)){
            return false;
        }
    }
    return true;
}

void dfs(int x){
    if (x==n)
    {
        ans++;
    }
    else
    {
        for(int i = 0; i<n; i++){
            row[x] = i;
            if (check(x)){
                dfs(x+1);
            }
        }
    }
}
int main(){
    cin >> n;
    dfs(0);
    cout << ans;
}