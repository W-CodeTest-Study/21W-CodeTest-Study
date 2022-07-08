#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int> > board, vector<int> moves) {
    int answer = 0, board_size = (int)board.size();
    vector<int> stack;
    int board_top[30] = {0,};

    for(int i=0;i<board_size;i++){
        for(int j=0;j<board_size;j++){
            if(board[j][i] != 0){
                board_top[i] = j;
                break;
            }
        }
    }

    // for(int i=0;i<board_size;i++){
    //     cout << board_top[i] << " ";
    // }
    // cout << endl;

    for(auto it : moves){
        if(board_top[it-1] != board_size){
            if(!stack.empty() && stack.back() == board[board_top[it-1]][it-1]){
                stack.pop_back();
                answer += 2;
            }
            else{
                stack.push_back(board[board_top[it-1]][it-1]);
            }
            board_top[it-1] += 1;
        }
    }

    return answer;
}

int main(){
    
    vector<vector<int> > board(5, vector<int>(5));
    vector<int> moves(8);

    int arr[8] = {1,5,3,5,1,2,1,4};
    int arr2[5][5] = {
        {0,0,0,0,0},
        {0,0,1,0,3},
        {0,2,5,0,1},
        {4,2,4,4,2},
        {3,5,1,3,1}
    };

    for(int i=0;i<8;i++){
        moves[i] = arr[i];
    }

    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            board[i][j] = arr2[i][j];
        }
    }

    cout << solution(board, moves) << "\n";

    return 0;
}