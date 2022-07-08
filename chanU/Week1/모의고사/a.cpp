#include <string>
#include <vector>
#include <iostream>

using namespace std;

class student{
private:
    int num;   //학번
    int score; //점수
    vector<int> &pattern; //패턴
public:
    student(int n, vector<int> &pattern);
    int get_score();
    void 채점하기(vector<int> &answer);
    int get_number();
};
student::student(int n, vector<int> &pattern)
    :num(n), score(0), pattern(pattern)
{
}
void student::채점하기(vector<int> &answers){
    int j=0;
    for(int i=0;i<answers.size();i++){
        if(this->pattern[j++ % (pattern.size())] == answers[i]){
            this->score += 4; // 21번이든 16번이든 4점!
        }
    }
}
int student::get_number(){
    return num;
}
int student::get_score(){
    return score;
}
vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> input;
    vector<int> one = {1,2,3,4,5};
    vector<int> two = {2,1,2,3,2,4,2,5};
    vector<int> three = {3,3,1,1,2,2,4,4,5,5};
    vector<student> stu;
    stu.push_back(student(1, one));
    stu.push_back(student(2, two));
    stu.push_back(student(3, three));
    int max = -1;
    
    for(int i = 0 ; i < stu.size(); i ++){
        stu[i].채점하기(answers);
    }
    
    for(auto s : stu)
        cout<< s.get_score() << " ";
    
    for(auto s : stu)
        if(max < s.get_score()){
            answer.clear();
            answer.push_back(s.get_number());
            max = s.get_score();
        }else if(max == s.get_score()){
            answer.push_back(s.get_number());
        }
    
    return answer;
}
