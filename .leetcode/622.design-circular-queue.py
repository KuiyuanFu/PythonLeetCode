# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#
# https://leetcode.com/problems/design-circular-queue/description/
#
# algorithms
# Medium (48.02%)
# Likes:    1305
# Dislikes: 154
# Total Accepted:    139.6K
# Total Submissions: 290.4K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' +
# '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# Design your implementation of the circular queue. The circular queue is a
# linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to the
# first position to make a circle. It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the
# spaces in front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the
# queue. But using the circular queue, we can use the space to store new
# values.
#
# Implementation the MyCircularQueue class:
#
#
# MyCircularQueue(k) Initializes the object with the size of the queue to be
# k.
# int Front() Gets the front item from the queue. If the queue is empty, return
# -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return
# -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return
# true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if
# the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
#
#
# You must solve the problem without using the built-in queue data structure in
# your programming language.
#
#
# Example 1:
#
#
# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear",
# "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]
#
# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4
#
#
#
# Constraints:
#
#
# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty,
# and isFull.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 构建一个循环队列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MyCircularQueue:
    def __init__(self, k: int):
        self.s = [None] * (k + 1)
        self.r = 0
        self.f = 0
        self.k = k + 1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.s[self.r] = value
        self.r = (self.r + 1 + self.k) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.f = (self.f + 1 + self.k) % self.k
        return True

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.s[(self.r - 1 + self.k) % self.k]
        return -1

    def Front(self) -> int:
        if not self.isEmpty():
            return self.s[self.f]
        return -1

    def isEmpty(self) -> bool:
        return self.r == self.f

    def isFull(self) -> bool:
        return (self.r + 1) % self.k == self.f


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end