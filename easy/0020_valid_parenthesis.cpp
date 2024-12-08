#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> parenMap = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        
        for (char c : s) {
            if (parenMap.count(c)) {
                if (!stk.empty() && stk.top() == parenMap[c])
                    stk.pop();
                else
                    return false;
            } else {
                stk.push(c);
            }
        }

        return stk.empty();
    }
};