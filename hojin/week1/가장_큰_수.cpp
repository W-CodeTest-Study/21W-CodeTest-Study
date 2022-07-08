#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare(const string & a, const string & b){
    if(a + b > b + a){
        return true;
    }
    return false;
}

string solution(vector<int> numbers) {

    int size = (int)numbers.size();
    string tmp;
    string answer;
    bool check  = false;
    vector<string> value;

    for(auto it : numbers){
        value.push_back(to_string(it));
    }

    sort(value.begin(), value.end(), compare);

    for(auto it : value){
        //cout << it << endl;
        answer += it;
        if(it != "0"){
            check = true;
        }
    }

    if(check == false){
        answer = "0";
        return answer;
    }
    
    return answer;
}

int main(){

    vector<int> numbers;

    // numbers.push_back(6);
    // numbers.push_back(10);
    // numbers.push_back(2);
    // numbers.push_back(37);
    // numbers.push_back(35);
    // numbers.push_back(32);
    // numbers.push_back(37);
    // numbers.push_back(33);
    // numbers.push_back(331);
    numbers.push_back(0);
    numbers.push_back(0);
    numbers.push_back(0);
    numbers.push_back(0);
    numbers.push_back(0);

    cout << solution(numbers) << "\n";



    return 0;
}