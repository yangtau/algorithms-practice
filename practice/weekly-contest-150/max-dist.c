#include <math.h>
#include <stdio.h>
#include <stdlib.h>

inline int check(int** grid, int size, int m, int n, int j, int i) {
    int x1 = j + m, x2 = j - m, y1 = i + n, y2 = i - n;
    return (x1 < size && x1 >= 0 && y1 < size && y1 >= 0 &&
            grid[x1][y1] == 1) ||
           (x2 < size && x2 >= 0 && y2 < size && y2 >= 0 &&
            grid[x2][y2] == 1) ||
           (x2 < size && x2 >= 0 && y1 < size && y1 >= 0 &&
            grid[x2][y1] == 1) ||
           (x1 < size && x1 >= 0 && y2 < size && y2 >= 0 && grid[x1][y2] == 1);
}
inline int max(int a, int b) {
    return a > b ? a : b;
}
int maxDistance(int** grid, int gridSize, int* gridColSize) {
    int far_dis = -1;
    for (int i = 0; i < gridSize; i++)
        for (int j = 0; j < gridSize; j++)
            if (grid[i][j] == 0) {
                int min_dist = 1;
                int max_dis =
                    max(gridSize - 1 - i, i) + max(gridSize - 1 - j, j);
                int flag = 0;
                for (; min_dist <= max_dis; min_dist++) {
                    for (int m = 0; m <= min_dist; m++) {
                        int n = min_dist - m;
                        if (check(grid, gridSize, m, n, i, j)) {
                            flag = 1;
                            break;
                        }
                    }
                    if (flag)
                        break;
                }
                if (flag && min_dist > far_dis)
                    far_dis = min_dist;
            }
    return far_dis;
}
