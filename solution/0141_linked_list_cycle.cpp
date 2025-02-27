#include <iostream>

#include "../common/ListNode.cpp"

using namespace std;

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return false;
        }
        ListNode *slow, *fast;
        slow = head;
        fast = head;
        do {
            if (fast->next == NULL || fast->next->next == NULL)   
                return false;
            slow = slow->next;
            fast = fast->next->next;
        } 
        while (slow != fast);
        return true;
    }
};