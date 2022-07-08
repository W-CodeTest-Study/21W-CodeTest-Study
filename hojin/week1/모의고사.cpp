#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int idx = 0, max_value = 0;
    int user_score[3] = {0,};
    int user1[5] = {1, 2, 3, 4, 5};
    int user2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
    int user3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    for(auto it : answers){
        if(idx == 5){
            idx = 0;
        }
        if(it == user1[idx]){
            user_score[0] += 1;
        }
        idx += 1;
    }

    idx = 0;
    for(auto it : answers){
        if(idx == 8){
            idx = 0;
        }
        if(it == user2[idx]){
            user_score[1] += 1;
        }
        idx += 1;
    }

    idx = 0;
    for(auto it : answers){
        if(idx == 10){
            idx = 0;
        }
        if(it == user3[idx]){
            user_score[2] += 1;
        }
        idx += 1;
    }

    max_value = *max_element(user_score, user_score+3);
    for(int i=0;i<3;i++){
        if(max_value == user_score[i]){
            answer.push_back(i+1);
        }
    }

    return answer;
}

int main(){

    vector<int> answers;
    answers.push_back(1);
    answers.push_back(2);
    answers.push_back(3);
    answers.push_back(4);
    answers.push_back(5);

    vector<int> answer(solution(answers));

    for(auto it : answer){
        cout << it << " ";
    }
    cout << endl;


    return 0;
}