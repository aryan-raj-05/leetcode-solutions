#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> table(26, 0);
        for (char c: magazine)
            table[c - 'a']++;
        for (char c: ransomNote)
            table[c - 'a']--;
        for (int i: table)
            if (i < 0) return false;
        return true;
    }
};