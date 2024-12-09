#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int top = 0;
        for (int iter = 1; iter < nums.size(); iter++) {
            if (nums[iter] != nums[top]) {
                nums[++top] = nums[iter];
            }
        }
        return (top + 1);
    }
};