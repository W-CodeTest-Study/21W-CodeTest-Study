#include <string>
#include <vector>
#include <iostream>
#include <cstring>
#include <queue>
#include <utility>

using namespace std;
using Pair = pair<int,int>;

int solution(int m, int n, vector<string> board) {
    int answer = 0, i = 0, j = 0, k = 0, check_idx = -1;
    queue<Pair> q;
    bool check = false;
    
    do{
        check = false;
        for(i=0;i<m-1;i++){
            for(j=0;j<n-1;j++){
                if(board[i][j] != '0' && board[i][j] == board[i][j+1] && board[i][j] == board[i+1][j] && board[i][j] == board[i+1][j+1]){
                    q.push({i,j});
                    q.push({i,j+1});
                    q.push({i+1,j});
                    q.push({i+1,j+1});
                    check = true;
                }
            }
        }

        while(!q.empty()){
            i = q.front().first;
            j = q.front().second;
            q.pop();
            if(board[i][j] != '0'){
                answer += 1;
            }
            board[i][j] = '0';
        }

        for(j=0;j<n;j++){
            check_idx = -1;
            for(i=m-1;i>=0;i--){
                if(board[i][j] == '0'){
                    for(k=i-1;k>=0;k--){
                        if(board[k][j] != '0'){
                            board[i][j] = board[k][j];
                            board[k][j] = '0';
                            break;
                        }
                    }
                }
            }
        }

    }while(check);

    return answer;
}

int main(){

    vector<string> board;
    //board.push_back("CCBDE");
    //board.push_back("AAADE");
    //board.push_back("AAABF");
    //board.push_back("CCBBF");
    board.push_back("AAAAAA");
    board.push_back("AABBAA");
    board.push_back("AABBAA");
    board.push_back("AAAAAA");
    board.push_back("AAACCA");
    board.push_back("AAACCA");


    cout << solution(6, 6, board) <<"\n";

    return 0;
}