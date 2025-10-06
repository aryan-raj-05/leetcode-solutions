#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    // counting sort method
    void sortColors(vector<int>& nums) {
        vector<int> bookkeeper(3, 0);
        for (int num: nums) bookkeeper[num]++;

        int numsIter = 0;
        for (int i = 0; i < 3; i++) {
            while (bookkeeper[i] > 0) {
                nums[numsIter++] = i;
                bookkeeper[i]--;
            }
        }
    }

    // dutch national flag problem
    void sortColors_dnf(vector<int>& nums) {
        int lo = 0, mid = 0, hi = nums.size() - 1;
        while (mid <= hi) {
            if (nums[mid] == 0) {
                swap(nums[lo++], nums[mid++]);
            } else if (nums[mid] == 2) {
                swap(nums[hi--], nums[mid]);
            } else {
                mid++;
            }
        }
    }
};