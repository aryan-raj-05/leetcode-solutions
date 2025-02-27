#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> um;

        um['I'] = 1;
        um['V'] = 5;
        um['X'] = 10;
        um['L'] = 50;
        um['C'] = 100;
        um['D'] = 500;
        um['M'] = 1000;

        int result = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i != s.size() - 1 && um[s[i]] < um[s[i + 1]]) {
                result -= um[s[i]];
                continue;
            }
            result += um[s[i]];
        }
        return result;
    }
};