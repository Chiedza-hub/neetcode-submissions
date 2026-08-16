/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *reversed = nullptr;

        while(head) {
            ListNode* next = head->next; //keep track of the next elem
            head->next = reversed; // attach to the back of new list
            reversed = head; // move the head forward
            head = next;  // move head forward   
        }
        return reversed;    
    }
};
