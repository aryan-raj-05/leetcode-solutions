#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums.at(nums.size() / 2);
    }

    int majorityElement2(vector<int>& nums) {
        unordered_map<int, int> table;
        for (int n : nums) {
            table[n]++;
        }

        int maxValue = 0;
        int maxKey = 0;
        for (auto& [key, value] : table) {
            if (value > maxValue) {
                maxValue = value;
                maxKey = key;
            }
        }

        return maxKey;
    }

    int majorityElement3(vector<int>& nums) {
        int candidate = -1;
        int votes = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (votes == 0) {
                candidate = nums.at(i);
                votes = 1;
            } else if (candidate == nums.at(i)) {
                votes++;
            } else {
                votes--;
            }
        }

        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums.at(i) == candidate) count++;
        }

        return (count > nums.size() / 2) ? candidate : -1;
    }
};

/*

1. sort the array and return the middle element                     => TC - O(nlogn), SC - O(1)
2. maintain a hash_map and return the element with largest value    => TP - O(n),     SC - O(n)
3. Boyer-Moore Majority Voting Algorithm                            => TC - O(n),     SC - O(1)

*/