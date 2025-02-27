#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return 0;
        }

        int lo = 0;
        int hi = nums.size() - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if      (nums[mid] == target)    return mid;
            else if (nums[mid] > target)     hi = mid - 1;
            else                             lo = mid + 1;
        }

        return nums[lo] < target ? lo + 1 : lo;
    }
};