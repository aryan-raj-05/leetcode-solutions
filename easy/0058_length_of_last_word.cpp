#include <iostream>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        if (s.size() == 1 && isalpha(s[0])) {
            return 1;
        }

        bool hasCountStart = false;
        int count = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] == ' ' && !hasCountStart) {
                continue;
            } else if (s[i] == ' ' && hasCountStart) {
                return count;
            } else {
                hasCountStart = true;
                count++;
            }
        }

        return count;
    }
};