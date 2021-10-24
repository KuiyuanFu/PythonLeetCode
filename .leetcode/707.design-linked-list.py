# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Medium (26.40%)
# Likes:    1098
# Dislikes: 998
# Total Accepted:    144.1K
# Total Submissions: 543.4K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
# '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val
# is the value of the current node, and next is a pointer/reference to the next
# node.
# If you want to use the doubly linked list, you will need one more attribute
# prev to indicate the previous node in the linked list. Assume all nodes in
# the linked list are 0-indexed.
#
# Implement the MyLinkedList class:
#
#
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the index^th node in the linked list. If
# the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of
# the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the
# linked list.
# void addAtIndex(int index, int val) Add a node of value val before the
# index^th node in the linked list. If index equals the length of the linked
# list, the node will be appended to the end of the linked list. If index is
# greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the index^th node in the linked list, if
# the index is valid.
#
#
#
# Example 1:
#
#
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
#
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
#
#
#
# Constraints:
#
#
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
# deleteAtIndex.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 设计链表。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Node:
    def __init__(self, val=0, pre: 'Node' = None, next: 'Node' = None) -> None:
        self.val = val
        self.pre = pre
        self.next = next

    def addNext(self, val):
        pn = Node(val=val, next=self.next, pre=self)
        self.next.pre = pn
        self.next = pn

    def deleteNext(self):
        pnn = self.next.next
        if pnn:
            pnn.pre = self
        self.next = pnn


class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1

        p = self.head.next
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        self.size += 1
        self.head.addNext(val)

    def addAtTail(self, val: int) -> None:
        self.size += 1
        self.tail.pre.addNext(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            pass
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            self.size += 1
            p = self.head
            for _ in range(index):
                p = p.next
            p.addNext(val)

    def deleteAtIndex(self, index: int) -> None:
        if self.size > 0 and 0 <= index < self.size:
            self.size -= 1
            p = self.head
            for _ in range(index):
                p = p.next
            p.deleteNext()


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()

    pass
# @lc main=end