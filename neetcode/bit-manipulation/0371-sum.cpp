class Solution {
public:
    // XORing gives sum without carry
    // Carry is found by ANDing the numbers
    int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
};
