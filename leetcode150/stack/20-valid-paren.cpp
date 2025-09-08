#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution {
    bool openPair(char c) {
        return c == '(' || c == '{' || c == '[';
    }

    bool match(char a, char b) {
        return  (a == '(' && b == ')') ||
                (a == '{' && b == '}') ||
                (a == '[' && b == ']');
    }
public:
    bool isValid(string s) {
        stack<char> stk;

        for (char c: s) {
            if (openPair(c)) stk.push(c);
            else if (stk.empty()) return false;
            else if (match(stk.top(), c)) stk.pop();
            else return false;
        }

        return stk.empty();
    }
};

int main() {
    string s = "{}[]";
    Solution sol;

    cout << sol.isValid(s) << "\n";
}