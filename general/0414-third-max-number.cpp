#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    // using sorting
    // Time Complexity = O(n log n)
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int countUnique = 1;
        int curNum = nums[nums.size() - 1];
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (nums[i] != curNum && countUnique == 2) {
                return nums[i];
            } else if (nums[i] != curNum && countUnique < 2) {
                countUnique++;
                curNum = nums[i];
            }
        }

        return *max_element(nums.begin(), nums.end());
    }
};
