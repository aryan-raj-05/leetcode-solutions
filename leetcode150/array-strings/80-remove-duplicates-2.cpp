#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int np = 1, sp = 0;
        int count = 1;
        for (; np < nums.size(); np++) {
            if (nums[np] == nums[sp] && count == 1) {
                nums[++sp] = nums[np];
                count++;
            } else if (nums[np] != nums[sp]) {
                nums[++sp] = nums[np];
                count = 1;
            }
        }
        return sp + 1;
    }
};