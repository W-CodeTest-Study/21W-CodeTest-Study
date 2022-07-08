#include <string>
#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare(deque<int> &a, deque<int> &b){ // 각 행의 size 를 기준으로 sort 진행
        if(a.size() > b.size()){
            return true;
        }
        else{
            return false;
        }
}

vector<int> solution(string s) {
    vector<int> answer;
    bool visit[100000] = {0,};
    bool check = false;
    deque<deque<int> > arr;
    deque<int> tmp;
    int count = 0, data = 0;

    arr.push_back(tmp);

    for(auto it : s){ // 문자열로 들어온 데이터를 정수형으로 가공하는 과정
        if(it == '}' && check == true){
            data /= 10;
            arr[count].push_back(data);
            arr.push_back(tmp);
            count += 1;
            check = false;
            data = 0;
        }
        else if(it >= 48 && it <= 57){ 
            data += it-'0';
            data *= 10;
            check = true;
        }
        else if(it == ',' && check == true){
            data /= 10;
            arr[count].push_back(data);
            data = 0;
        }
    }

    sort(arr.begin(),arr.end(),compare);

    for(int i=count-1;i>=0;i--){
        for(auto it : arr[i]){
            if(visit[it] == false){
                visit[it] = true;
                answer.push_back(it); // 최종 정답 vector를 생성하는 과정 이때 이미 삽입한 원소의 경우 visit 배열을 이용해 검사하여 생략한다.
            }
        }
    }

    return answer;
}

int main(){

    vector<int> value(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"));

    for(auto it : value){
        cout << it << " ";
    }
    cout << endl;

    return 0;
}