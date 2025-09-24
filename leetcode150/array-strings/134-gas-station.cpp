#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // brute force complete search
    // Time complexity: O(n^2)
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        for (int start_ind = 0; start_ind < n; start_ind++) {
            int cur_ind = start_ind;
            int cur_gas = 0;
            do {
                cur_gas += gas[cur_ind];
                cur_gas -= cost[cur_ind];
                cur_ind = (cur_ind + 1) % n;
            } while (cur_ind != start_ind && cur_gas > 0);

            if (cur_ind == start_ind && cur_gas >= 0) {
                return start_ind;
            }
        }
        return -1;
    }

    // 1. total gas that can be filled should be greater than total cost to travel or at least equal
    // 2. start index can't be the one where (gas[i] - cost[i]) < 0
    // 3. if we find a good starting point, say 'A', then keep track of (gas[i] - cost[i])
    // 4. if at any point 'B' it goes zero then, any points ['A' to 'B'] can't be starting points
    // 5. set start point to the next index after 'B'
    int canCompleteCircuit_greedy(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int total_surplus = 0;
        int surplus = 0;
        int start = 0;

        for (int i = 0; i < n; i++) {
            total_surplus += gas[i] - cost[i];
            surplus += gas[i] - cost[i];
            if (surplus < 0) {
                surplus = 0;
                start = i + 1;
            }
        }

        return (total_surplus < 0) ? -1 : start;
    }
};
