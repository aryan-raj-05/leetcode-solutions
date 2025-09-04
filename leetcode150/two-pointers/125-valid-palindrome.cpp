#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            while (i < j && !isAlphaNumeric(s.at(i))) i++;
            while (i < j && !isAlphaNumeric(s.at(j))) j--;
            if (!equal(s.at(i), s.at(j))) return false;
            i++;
            j--;
        }
        return true;
    }
private:
    bool equal(char c, char h) {
        return lower(c) == lower(h);
    }

    char lower(char c) {
        if (c >= 'A' && c <= 'Z') return c + 32;
        return c;
    }

    bool isAlphaNumeric(char c) {
        return (c >= 'a' && c <= 'z')
            || (c >= 'A' && c <= 'Z')
            || (c >= '0' && c <= '9');
    }
};