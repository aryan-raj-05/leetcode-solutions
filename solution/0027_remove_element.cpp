#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int top = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val)
                nums[++top] = nums[i];
        }
        return (top + 1);
    }
};