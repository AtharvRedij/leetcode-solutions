'''
URL: https://leetcode.com/problems/merge-two-sorted-lists/

Difficulty: Easy

Description: Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, l1, l2):
        new_list = None
        new_list_tail = None

        ptr1 = l1
        ptr2 = l2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                if new_list == None:
                    new_list = ptr1
                    new_list_tail = new_list
                else:
                    new_list_tail.next = ptr1
                    new_list_tail = ptr1
                ptr1 = ptr1.next
            else:
                if new_list == None:
                    new_list = ptr2
                    new_list_tail = new_list
                else:
                    new_list_tail.next = ptr2
                    new_list_tail = ptr2
                ptr2 = ptr2.next

        while ptr1:
            if new_list == None:
                new_list = ptr1
                new_list_tail = new_list
            else:
                new_list_tail.next = ptr1
                new_list_tail = ptr1

            ptr1 = ptr1.next

        while ptr2:
            if new_list == None:
                new_list = ptr2
                new_list_tail = new_list
            else:
                new_list_tail.next = ptr2
                new_list_tail = ptr2
            ptr2 = ptr2.next

        return new_list
