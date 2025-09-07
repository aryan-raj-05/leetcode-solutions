#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> romanToInt = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int sum = 0;
        for (int i = 0; i < s.size();) {
            if (i != s.size() - 1 && romanToInt[s[i]] < romanToInt[s[i + 1]]) {
                sum += (romanToInt[s[i + 1]] - romanToInt[s[i]]);
                i += 2;
                continue;
            }
            sum += romanToInt[s[i++]];
        }

        return sum;
    }

    int romanToInt2(string s) {
        int values[256] = {};
        values['I'] = 1;
        values['V'] = 5;
        values['X'] = 10;
        values['L'] = 50;
        values['C'] = 100;
        values['D'] = 500;
        values['M'] = 1000;

        int sum = 0;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            int curr = values[s[i]];
            int next = (i + 1 < n) ? values[s[i + 1]] : 0;
            if (next > curr) {
                sum -= curr;
            } else {
                sum += curr;
            }
        }
        return sum;
    }
};