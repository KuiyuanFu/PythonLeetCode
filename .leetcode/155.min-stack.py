# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (47.17%)
# Likes:    5177
# Dislikes: 486
# Total Accepted:    735.8K
# Total Submissions: 1.6M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
#  '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
# Implement the MinStack class:
#
#
# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
#
#
#
# Example 1:
#
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
#
# Constraints:
#
#
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
#
#
#

# @lc tags=stack;design

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 设计一个栈，有 push pop top getMin 操作。
# 使用链表实现。
#
# @lc idea=end

# @lc group=stack;design

# @lc rank=10

# @lc code=start


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
        self.min = self.val
        if self.next:
            self.min = min(self.val, self.next.min)


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        self.head = Node(val, self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.pop()
    obj.push(4)
    param_3 = obj.top()
    param_4 = obj.getMin()
    pass
# @lc main=end