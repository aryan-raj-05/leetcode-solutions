#include <cmath>

class Solution {
public:
    int mySqrt(int x) {
        double lo = 0.0;
        double hi = x;
        while (std::abs(lo - hi) > 0.000001) {
            double mid = lo + (hi - lo) / 2;
            if ((mid * mid) > x) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        return static_cast<int>(std::floor(hi));
    }
};