#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(string s) {
    int answer = s.length(), len = s.length(), count = 1, tmp = 0;
    string sub_string, sub_string2;

    for(int i=1;i<=len/2;i++){
        count = 1, tmp = 0;
        sub_string = s.substr(0,i);

        for(int j=i;j<len;j+=i){
            sub_string2 = s.substr(j,i);

            if(sub_string == sub_string2){
                count += 1;
            }
            else{
                if(count != 1){
                    tmp += to_string(count).length();
                }
                tmp += sub_string.length();
                sub_string = sub_string2;

                count = 1;
            }
            if(j + i >= len){
                tmp += s.substr(j,i).length();
                if(count != 1){
                    tmp += to_string(count).length();
                }
            }
        }
        answer = min(answer, tmp);
    }

    return answer;
}

int main(){

    string input_data;

    cin >> input_data;
   
    cout << solution(input_data) << "\n";

    return 0;
}