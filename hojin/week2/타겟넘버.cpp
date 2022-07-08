#include <iostream>
#include <vector>

using namespace std;

int n_size, counter;

void dfs(vector<int> numbers, int idx, int value, int target){

    if(n_size != idx){
        dfs(numbers, idx+1, value + numbers[idx],target);
        dfs(numbers, idx+1, value + (numbers[idx] * -1),target);
    }
    else if(target == value){
        counter += 1;
    }

}

int solution(vector<int> numbers, int target) {
    int answer = 0;

    n_size = (int)numbers.size();

    dfs(numbers, 0, 0, target);

    return counter;
}

int main(){

    vector<int> arr;
    arr.push_back(1);
    arr.push_back(1);
    arr.push_back(1);
    arr.push_back(1);
    arr.push_back(1);

    cout << solution(arr,3) << "\n";



    return 0;
}