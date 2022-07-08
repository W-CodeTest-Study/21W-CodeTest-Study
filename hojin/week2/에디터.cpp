#include <list>
#include <iostream>
#include <string>

using namespace std;

int main(){

    string input_data;
    list<char> editor;
    list<char>::iterator iter;
    int M = 0;
    char commmad, insert_data;

    cin >> input_data;

    for(auto it : input_data){
        editor.push_back(it);
    }
    iter = editor.end();
    
    cin >> M;
    
    for(int i=0;i<M;i++){
        cin >> commmad;
        if(commmad == 'P'){
            cin >> insert_data;
            editor.insert(iter,insert_data);
            //cout << *iter << endl;
        }
        else if(commmad == 'L'){
            if(iter != editor.begin()){
                iter --;
                //cout << *iter << endl;
            }
        }
        else if(commmad == 'D'){
            if(iter != editor.end()){
                iter ++;
            }
        }
        else if(commmad == 'B'){
            if(iter != editor.begin()){
                iter --;
                iter = editor.erase(iter);
            }
        }
    }
   
    for(auto it : editor){
        cout << it;
    }
    cout << "\n";

    return 0;
}