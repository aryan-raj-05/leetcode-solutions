#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int curMinInd = 0;
        for (int i = 0; i < prices.size(); i++) {
            curMinInd = (prices[i] < prices[curMinInd]) ? i : curMinInd;
            profit = max(profit, (prices[i] - prices[curMinInd]));
        }
        return profit;
    }
};