#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> charTable(26, 0);
        for (char c : t) charTable[c - 'a']++;
        for (char c : s) charTable[c - 'a']--;
        for (int i : charTable)
            if (i < 0) return false;
        return true;
    }
};