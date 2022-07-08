#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool check_func(string u){

    vector<char> stack;

    for(auto it : u){
        if(!stack.empty() && stack.back() == '(' && it == ')'){
            stack.pop_back();
        }
        else{
            stack.push_back(it);
        }
    }
    if(!stack.empty()){
        return false;
    }
    return true;
}

string solution(string p) {

    int left = 0, right = 0, range = 0;
    bool check = false;
    string u = "", v = "", tmp = "";

    if(p == ""){
        return "";
    }

    for(auto it : p){
        if(check){
            v += it;
        }
        else{
            u += it;
            if(it == ')'){ //
                right += 1;
            }
            else{
                left += 1;
            }
            if(right == left){
                check = true;
            }
        }
    }

    if(check_func(u)){
        u += solution(v); 
    }
    else{
        tmp = "(" + solution(v) + ")";
 
        range = (int)u.size() - 1;
        for(int i=1;i<range;i++){
            if(u[i] == ')'){
                tmp += '(';
            }
            else{
                tmp += ')';
            }
        }
        return tmp;
    }

    return u;
}

int main(){

    cout << solution("()") << "\n";


    return 0;
}