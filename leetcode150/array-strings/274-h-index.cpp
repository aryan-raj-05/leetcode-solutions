#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
// citations = [3,0,6,1,5], h-index = 3

class Solution {
public:
    // 1. start with x = citations.length
    // 2. count y = number of entries equal or greater than x
    // 3. if y >= x, return x
    // 4. else x--
    // Time Complexity - O(n^2)
    int hIndex(vector<int>& citations) {
        int h = citations.size();
        while (h > 0) {
            int count = 0;
            for (int i = 0; i < citations.size(); i++) {
                if (citations[i] >= h) count++;
            }
            if (count >= h) return h;
            h--;
        }
        return 0;
    }

    // sort the citations array
    // find the h index by interating through array in reverse
    // time complexity - O(nlogn)
    int hIndexSort(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int h = citations.size();
        int count = 0, i = citations.size() - 1;
        while (1) {
            if (count == h) return h;
            if (i < 0) return 0;
            if (citations[i] >= h) { count++; i--; }
            else h--;
        }
        return 0;
    }

    // counting sort method
    int hIndexCount(vector<int>& citations) {
        
    }
};

int main() {
    vector<int> citations = {1};

    Solution s;
    cout << s.hIndexSort(citations) << "\n";
}