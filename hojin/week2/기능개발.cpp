#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int idx = 0, size = (int)progresses.size(), count = 0;

    while(idx != size){
        count = 0;
        for(int i=idx;i<size;i++){
            progresses[i] += speeds[i];
            if(i == idx && progresses[i] >= 100){
                count += 1;
                idx += 1;
            }
        }
        if(count !=0){
            answer.push_back(count);
        }
    }
    return answer;
}

int main(){

    vector<int> progresses, speeds;

    progresses.push_back(93);
    progresses.push_back(30);
    progresses.push_back(55);

    speeds.push_back(1);
    speeds.push_back(30);
    speeds.push_back(5);

    vector<int> value(solution(progresses, speeds));

    for(auto it : value){
        cout << it << " ";
    }
    cout << endl;

    return 0;
}