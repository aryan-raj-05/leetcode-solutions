#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    // using a set
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> uset;
        for (int i: nums) {
            if (uset.find(i) == uset.end()) uset.insert(i);
            else return true;
        }
        return false;
    }
};