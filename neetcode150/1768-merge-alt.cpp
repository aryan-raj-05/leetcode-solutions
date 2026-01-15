#include <string>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i = 0, j = 0;
        bool button = true; // 1 = true, 2 = false
        string result;
        result.reserve(word1.size() + word2.size());

        while (i < word1.size() && j < word2.size()) {
            if (button) result += word1.at(i++);
            else result += word2.at(j++);
            button = !button;
        }

        while (i < word1.size()) result += word1.at(i++);
        while (j < word2.size()) result += word2.at(j++);

        return result;
    }
};
