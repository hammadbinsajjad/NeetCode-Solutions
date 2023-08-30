#include <bits/stdc++.h>
using namespace std;

class Solution {
    int res = 0;
    map<int, int> vs;
public:
    int bt(int cur, int target, vector<int>& nums) {
        if (target < cur) {
            return 0;
        }
        if (target == cur) {
            res += 1;
            return 1;
        }

        if (vs.find(cur) != vs.end()) {
            res += vs[cur];
            return vs[cur];
        }
        
        int combs = 0;
        for (auto i:nums) {
            combs += bt(cur + i, target, nums);
        }

        vs[cur] = combs;
        return combs;
    }

    int combinationSum4(vector<int>& nums, int target) {
        bt(0, target, nums);
        return res;
    }
};