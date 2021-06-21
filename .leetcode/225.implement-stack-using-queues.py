# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (48.37%)
# Likes:    1144
# Dislikes: 697
# Total Accepted:    226.9K
# Total Submissions: 466.6K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a last in first out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal queue (push,
# top, pop, and empty).
#
# Implement the MyStack class:
#
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
#
#
# Notes:
#
#
# You must use only standard operations of a queue, which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue), as long as you
# use only a queue's standard operations.
#
#
#
# Example 1:
#
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
#
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
#
#
#
# Constraints:
#
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
#
#
#
# Follow-up: Can you implement the stack using only one queue?
#
#

# @lc tags=stack;design

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 实现一个后进先出的栈。
# 直接数组，加一个容量。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MyStack:
    def __init__(self):
        self.length = 0
        self.stack = []

    def push(self, x: int) -> None:
        self.length += 1
        self.stack.append(x)

    def pop(self) -> int:
        self.length -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.length == 0


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end