#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for (int stone : stones) {
            pq.push(stone);
        }

        while (pq.size() > 1) {
            int l1 = pq.top(); pq.pop();
            int l2 = pq.top(); pq.pop();

            if (l1 != l2) {
                pq.push(abs(l1 - l2));
            }
        }

        return pq.empty() ? 0 :  pq.top();
    }
};
