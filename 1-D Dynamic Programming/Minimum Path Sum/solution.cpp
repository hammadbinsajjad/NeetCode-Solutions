#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();

        vector<int> current(m, 2e6);
        vector<int> next(m, 2e6);

        current[0] = grid[0][0];
        for (int i = 0;i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (i < n - 1) next[j] = min(next[j], current[j] + grid[i + 1][j]);
                if (j < m - 1) current[j + 1] = min(current[j + 1], current[j] + grid[i][j + 1]);
            }
            if (i == n - 1) break;
            current = next;
            next = vector<int>(m, 2e6);
        }

        return current[m - 1];
    }
};