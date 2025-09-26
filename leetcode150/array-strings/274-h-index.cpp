#include <algorithm>
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
    // find the h index by iterating through array in reverse
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
        vector<int> sortedCitations = countSort(citations);
        int h = sortedCitations.size();
        int count = 0, i = sortedCitations.size() - 1;
        while (1) {
            if (count == h) return h;
            if (i < 0) return 0;
            if (sortedCitations[i] >= h) { count++; i--; }
            else h--;
        }
        return 0;
    }

    vector<int> countSort(const vector<int>& citations) {
        int n = citations.size();
        int maxVal = *max_element(citations.begin(), citations.end());

        vector<int> aux(maxVal + 1, 0);
        for (int num : citations)            aux[num]++;
        for (int i = 1; i < aux.size(); i++) aux[i] += aux[i - 1];

        vector<int> output(n);
        for (int i = n - 1; i >=0 ; i--)
            output[--aux[citations[i]]] = citations[i];
        return output;
    }
};