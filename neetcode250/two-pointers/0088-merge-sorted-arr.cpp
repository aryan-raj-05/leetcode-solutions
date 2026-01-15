#include <vector>
using namespace std;

/* Two Ways of solving the problem
    1. By creating an auxiliary array where the element would be copied in sorted order
       and then copied back to nums1
       Time: O(m + n), Space: O(n)
    2. Sorting it in backwards direction
       Time: O(m + n), Space: O(1)
*/
class Solution {
public:
    // method 1
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int len = nums1.size();
        vector<int> aux(len, 0);
        int i = 0, j = 0, k = 0;

        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) aux[k] = nums1[i++];
            else aux[k] = nums2[j++];
            k++;
        }

        while (i < m) aux[k++] = nums1[i++];
        while (j < n) aux[k++] = nums2[j++];
        for (int i = 0; i < len; i++) nums1[i] = aux[i];
    }

    // method 2
    void merge2(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1, j = n - 1, k = nums1.size() - 1;

        while (i >= 0 && j >= 0) {
            if (nums1[i] < nums2[j]) nums1[k] = nums2[j--];
            else nums1[k] = nums1[i--];
            k--;
        }

        while (j >= 0) nums1[k--] = nums2[j--];
    }
};