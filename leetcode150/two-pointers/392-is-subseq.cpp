#include <string>
using namespace std;

class Solution {

public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        while (i < s.size()) {
            if (j >= t.size()) return false;
            if (s.at(i) == t.at(j++)) {
                i++;
            }
        }
        return true;
    }
};