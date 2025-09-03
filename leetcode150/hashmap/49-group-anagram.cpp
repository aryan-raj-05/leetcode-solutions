#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        vector<bool> isUsed(strs.size(), false);

        for (int i = 0; i < strs.size(); i++) {
            if (isUsed[i]) continue;

            vector<string> tmp;
            for (int j = 0; j < strs.size(); j++) {
                if (isUsed[j]) continue;
                if (isAnagram(strs.at(i), strs.at(j))) {
                    tmp.push_back(strs.at(j));
                    isUsed[j] = true;
                }
            }
            result.push_back(tmp);
        }

        return result;
    }

private:
    bool isAnagram(string &s, string &t) {
        if (s.size() != t.size()) return false;
        vector<int> charTable(26, 0);
        for (char c : s) charTable[c - 'a']++;
        for (char c : t) charTable[c - 'a']--;
        for (int i : charTable)
            if (i < 0) return false;
        return true;
    }
};
