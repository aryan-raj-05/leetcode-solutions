#include <iostream>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    // iterative
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return nullptr;
        auto reversedList = new ListNode(head->val);

        for (auto p = head->next; p != nullptr; p = p->next) {
            auto tmpNode = new ListNode(p->val, reversedList);
            reversedList = tmpNode;
        }

        return reversedList;
    }
};

int main() {
    auto singleElementList = new ListNode(4);

    Solution s;

    auto reversedList = s.reverseList(singleElementList);
    std::cout << reversedList->val << "\n";
}