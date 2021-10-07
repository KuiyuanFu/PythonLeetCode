# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#
# https://leetcode.com/problems/design-circular-deque/description/
#
# algorithms
# Medium (56.76%)
# Likes:    534
# Dislikes: 52
# Total Accepted:    34.7K
# Total Submissions: 61K
# Testcase Example:  '["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n' +
# '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# Design your implementation of the circular double-ended queue (deque).
#
# Implement the MyCircularDeque class:
#
#
# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the
# operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the
# operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true
# if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if
# the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque
# is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is
# empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
# "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 2, true, true, true, 4]
#
# Explanation
# MyCircularDeque myCircularDeque = new MyCircularDeque(3);
# myCircularDeque.insertLast(1);  // return True
# myCircularDeque.insertLast(2);  // return True
# myCircularDeque.insertFront(3); // return True
# myCircularDeque.insertFront(4); // return False, the queue is full.
# myCircularDeque.getRear();      // return 2
# myCircularDeque.isFull();       // return True
# myCircularDeque.deleteLast();   // return True
# myCircularDeque.insertFront(4); // return True
# myCircularDeque.getFront();     // return 4
#
#
#
# Constraints:
#
#
# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 2000 calls will be made to insertFront, insertLast, deleteFront,
# deleteLast, getFront, getRear, isEmpty, isFull.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 实现循环双向队列。
# 数组，两个指针，
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k + 1
        self.s = [None] * self.k
        self.f = self.k - 1
        self.r = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.f = (self.f + 1) % self.k
        self.s[self.f] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.r = (self.r - 1 + self.k) % self.k
        self.s[self.r] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.f = (self.f - 1 + self.k) % self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.r = (self.r + 1) % self.k
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[self.f]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[self.r]

    def isEmpty(self) -> bool:
        return (self.f + 1) % self.k == self.r

    def isFull(self) -> bool:
        return (self.f + 2) % self.k == self.r


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    # print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end