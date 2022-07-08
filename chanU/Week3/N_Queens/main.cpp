#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;

class bt{
public:
    int col;
    int row;
    bt(int col, int row)
    : col(col), row(row)
    {}
};

int main(void){
    int N, answer = 0;
    cin >> N;

    vector<int> col(N, 0);
    stack<class bt *> s;

    for(int i = 0; i < N; i++)
    {
        s.push(new class bt(0, i));
    }

    while(!s.empty())
    {
        class bt & pop = *(s.top());
        s.pop();

        col[pop.col] = pop.row;
        //printf("%d %d\n", pop.col, pop.row);

        if(pop.col == N - 1){
            answer++;
            goto end;
        }

        for(int i = 0; i < N ; i++){
            bool pruned = false;
            
            col[pop.col + 1] = i;
            
            for(int j = 0; j <= pop.col; j++){
                if(col[pop.col + 1] == col[j] || abs(col[j] - i) == abs(j - pop.col - 1)){
                    pruned = true;
                    break;
                }
            }
            
            if(!pruned){
                s.push(new class bt(pop.col + 1, i));
            }
        }
end:
        delete &pop;
    }

    cout<<answer<<endl;
}
