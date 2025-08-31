#include <vector>
using namespace std;

class Solution {
private:
    void reverse(vector<int>& nums, int i, int j) { // both i and j are inclusive
        int lo = i, hi = j;
        while (lo < hi) {
            int temp = nums[lo];
            nums[lo] = nums[hi];
            nums[hi] = temp;
            lo++; hi--;
        }
    }
public:
    // 1st method
    void rotate(vector<int>& nums, int k) {
        vector<int> aux(nums.size());
        k = k % nums.size();
        int fh = 0, sh = nums.size() - k;
        int i = 0;
        while (sh < nums.size()) {
            aux[i++] = nums[sh++];
        }

        while (fh < nums.size() - k) {
            aux[i++] = nums[fh++];
        }

        for (int i = 0; i < nums.size(); i++) {
            nums[i] = aux[i];
        }
    }

    // 2nd method
    // 1234 567 => 4321 765 => 5671234
    void rotateOpt(vector<int>& nums, int k) {
        k = k % nums.size();
        int l = nums.size();
        reverse(nums, 0, l - k - 1);
        reverse(nums, l - k, l - 1);
        reverse(nums, 0, l - 1);
    }
};