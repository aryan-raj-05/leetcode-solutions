class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while (n > 0) {
            // n&1 -> gives the LSB(least significant bit / last bit)
            if ((n&1) & 1) count++;
            n >>= 1;
        }
        return count;
    }

    int brian_kern(int n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }
};
