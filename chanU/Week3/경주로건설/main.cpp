#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

int N = 0;

// d 는 방향 상하좌우 각각 1234임

class pos{
public:
    int x;
    int y;
    int d;
    int cost;
    pos(int x, int y, int d, int cost)
        : x(x), y(y), d(d), cost(cost) {}
};

int solution(vector<vector<int>> board) {
    N = board.size();
    vector<vector<int>> cost(N, vector<int>(N, 0));
    stack<class pos *> s;
    
    if(!board[1][0])
        s.push(new pos(1, 0, 2, 100));
    if(!board[0][1])
        s.push(new pos(0, 1, 4, 100));
    
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cost[i][j] = -1;
    
    cost[0][0] = 0;
    
    while(!s.empty()){
        class pos & cur = *(s.top());
        int & c = cost[cur.x][cur.y];
        s.pop();
        
        if(c == -1 || c >= cur.cost){
            c = cur.cost;
        }else
            continue;
        
        switch (cur.d)
        {
        case 1:
            if (cur.x - 1 >= 0 && !board[cur.x - 1][cur.y])
                s.push(new pos(cur.x - 1, cur.y, 1, cur.cost + 100));
            if (cur.y + 1 < N && !board[cur.x][cur.y + 1])
                s.push(new pos(cur.x, cur.y + 1, 4, cur.cost + 600));
            if (cur.y - 1 >= 0 && !board[cur.x][cur.y - 1])
                s.push(new pos(cur.x, cur.y - 1, 3, cur.cost + 600));
            break;
        case 2:
            if (cur.x + 1 < N && !board[cur.x + 1][cur.y])
                s.push(new pos(cur.x + 1, cur.y, 2, cur.cost + 100));
            if (cur.y + 1 < N && !board[cur.x][cur.y + 1])
                s.push(new pos(cur.x, cur.y + 1, 4, cur.cost + 600));
            if (cur.y - 1 >= 0 && !board[cur.x][cur.y - 1])
                s.push(new pos(cur.x, cur.y - 1, 3, cur.cost + 600));
            break;
        case 3:
            if (cur.y - 1 >= 0 && !board[cur.x][cur.y - 1])
                s.push(new pos(cur.x, cur.y - 1, 3, cur.cost + 100));
            if (cur.x + 1 < N && !board[cur.x + 1][cur.y])
                s.push(new pos(cur.x + 1, cur.y, 2, cur.cost + 600));
            if (cur.x - 1 >= 0 && !board[cur.x - 1][cur.y])
                s.push(new pos(cur.x - 1, cur.y, 1, cur.cost + 600));
            break;
        case 4:
            if (cur.y + 1 < N && !board[cur.x][cur.y + 1])
                s.push(new pos(cur.x, cur.y + 1, 4, cur.cost + 100));
            if (cur.x + 1 < N && !board[cur.x + 1][cur.y])
                s.push(new pos(cur.x + 1, cur.y, 2, cur.cost + 600));
            if (cur.x - 1 >= 0 && !board[cur.x - 1][cur.y])
                s.push(new pos(cur.x - 1, cur.y, 1, cur.cost + 600));
            break;
        }
end:
        delete &cur;
    }
    
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++)
            printf("%d ", cost[i][j]);
        printf("\n");
    }
    
    return cost[N - 1][N - 1];
}
