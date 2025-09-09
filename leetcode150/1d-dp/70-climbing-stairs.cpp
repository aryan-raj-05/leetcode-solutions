class Solution {
public:
    int climbStairs(int n) {
        if (n == 2 || n == 1) return n;
        long long f1 = 1LL, f2 = 2LL;
        for (int i = 1; i < n; i++) {
            long long temp = f1 + f2;
            f1 = f2;
            f2 = temp;
        }
        return (int)f1;
    }
};

/*
    f(1) = 1;
    f(2) = 2;
    f(3) = f(2) + f(1) = 3
    f(4) = f(3) + f(2) = 5, 
        1+1+1+1
        1+2+1
        2+1+1
        1+1+2
        2+2
*/