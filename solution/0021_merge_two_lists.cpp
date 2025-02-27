#include <iostream>

#include "../common/ListNode.cpp"

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* res = new ListNode();
        ListNode* iter = res;

        while (list1 != NULL && list2 != NULL) {
            if (list1->val < list2->val) {
                iter->next = new ListNode(list1->val);
                iter = iter->next;
                list1 = list1->next;
            } else {
                iter->next = new ListNode(list2->val);
                iter = iter->next;
                list2 = list2->next;
            }
        }

        while (list1 != NULL) {
            iter->next = new ListNode(list1->val);
            iter = iter->next;
            list1 = list1->next;
        }

        while (list2 != NULL) {
            iter->next = new ListNode(list2->val);
            iter = iter->next;
            list2 = list2->next;
        }

        ListNode* ans = res->next;
        delete res;
        return ans;
    }
};