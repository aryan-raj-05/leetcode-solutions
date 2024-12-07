#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (um.find(complement) != um.end()) {
                result.push_back(i);
                result.push_back(um[complement]);
                return result;
            }
            um[nums[i]] = i;
        }

        return result;
    }    
};
