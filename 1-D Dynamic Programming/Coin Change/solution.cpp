#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> dp = vector<int>(1e4 + 1, -1);
    int solve(int target, vector<int>& nums) {
        if (target < 0) return 1e9;
        if (target == 0) return 0;

        if (dp[target] != -1) return dp[target];

        int best = 1e9;
        for (int n:nums) {
            best = min(best, solve(target - n, nums));
        }
        best += 1;
        dp[target] = best;
        return best;
    }

    int coinChange(vector<int>& coins, int amount) {
        int res = solve(amount, coins);
        if (res >= 1e9) return -1;
        else return res;
    }
};