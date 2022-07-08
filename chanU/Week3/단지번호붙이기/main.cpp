#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(void) {
    int N, danji = 1;
    queue<char> x;
    queue<char> y;
    cin >> N;
    vector<vector<int>> map(N, vector<int>(N, 0));

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            scanf("%1d", &map[i][j]);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            if (map[i][j] > 0) {
                x.push(i);
                y.push(j);
                map[i][j] = -danji;
            }
            else
                continue;

            while (!x.empty())
            {
                int pos_x = x.front();
                int pos_y = y.front();

                x.pop(); y.pop();

                if (pos_x - 1 >= 0 && map[pos_x - 1][pos_y] > 0) {
                    x.push(pos_x - 1);
                    y.push(pos_y);

                    map[pos_x - 1][pos_y] = -danji;
                }
                if (pos_x + 1 < N && map[pos_x + 1][pos_y] > 0) {
                    x.push(pos_x + 1);
                    y.push(pos_y);

                    map[pos_x + 1][pos_y] = -danji;
                }
                if (pos_y - 1 >= 0 && map[pos_x][pos_y - 1] > 0) {
                    x.push(pos_x);
                    y.push(pos_y - 1);

                    map[pos_x][pos_y - 1] = -danji;
                }
                if (pos_y + 1 < N && map[pos_x][pos_y + 1] > 0) {
                    x.push(pos_x);
                    y.push(pos_y + 1);

                    map[pos_x][pos_y + 1] = -danji;
                }
            }

            danji++;
        }

    vector<int> numOfHome(danji - 1, 0);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (map[i][j] != 0)
                numOfHome[-map[i][j] - 1]++;

    printf("%d\n", danji - 1);

    sort(numOfHome.begin(), numOfHome.end());

    for (auto n : numOfHome)
        printf("%d\n", n);
}
