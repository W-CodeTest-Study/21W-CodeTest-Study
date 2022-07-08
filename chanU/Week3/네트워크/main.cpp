#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 1;
    vector<int> networks(n, 0);
    stack<int> s;
    
    for(int i = 0; i < n ; i++){
        if(networks[i])
            continue;
        s.push(i);
    
        while(!s.empty()){
            int idx = s.top();
            s.pop();
            networks[idx] = answer;
        
            for(int j = 0 ; j < n; j++){
                if(computers[idx][j]){
                    if(!networks[j])
                        s.push(j);
                    networks[j] = answer;
                }
            }
        }
        answer++;
    }
    
    return answer - 1;
}
