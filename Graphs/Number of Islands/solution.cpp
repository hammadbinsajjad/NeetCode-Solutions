#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // Using Iterative DFS
        int res = 0;
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    stack<pair<int, int>, vector<pair<int, int>>> st;
                    st.push(pair<int, int>{i, j});
                    while (!st.empty()) {
                        pair<int, int> el = st.top();
                        st.pop();

                        grid[el.first][el.second] = '0';
                        int k = el.first, l = el.second;

                        if (k - 1 >= 0 && grid[k -  1][l] == '1') st.push(pair<int, int>{k - 1, l});
                        if (l - 1 >= 0 && grid[k][l - 1] == '1') st.push(pair<int, int>{k, l -1 });
                        if (k + 1 < n && grid[k + 1][l] == '1') st.push(pair<int, int>{k + 1, l});
                        if (l + 1 < m && grid[k][l + 1] == '1') st.push(pair<int, int>(k, l + 1));
                    }
                }
            }
        } 

        return res;
    }
};