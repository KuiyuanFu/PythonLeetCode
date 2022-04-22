# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#
# https://leetcode.com/problems/maximum-frequency-stack/description/
#
# algorithms
# Hard (66.38%)
# Likes:    3585
# Dislikes: 54
# Total Accepted:    124.2K
# Total Submissions: 187K
# Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' +
# '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
#
# Design a stack-like data structure to push elements to the stack and pop the
# most frequent element from the stack.
#
# Implement the FreqStack class:
#
#
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the
# stack.
#
# If there is a tie for the most frequent element, the element closest to the
# stack's top is removed and returned.
#
#
#
#
#
# Example 1:
#
#
# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop",
# "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]
#
# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
# [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is
# closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
# [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is
# closest to the top. The stack becomes [5,7].
#
#
#
# Constraints:
#
#
# 0 <= val <= 10^9
# At most 2 * 10^4 calls will be made to push and pop.
# It is guaranteed that there will be at least one element in the stack before
# calling pop.
#
#
#

# @lc tags=heap;breadth-first-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 最经常访问的元素。
# 直接堆。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class FreqStack:

    def __init__(self):
        self.numbers = defaultdict(int)
        self.heap = []
        self.callTimes = 0

    def push(self, val: int) -> None:
        self.numbers[val] -= 1
        self.callTimes -= 1
        heappush(self.heap, (self.numbers[val], self.callTimes, val))

    def pop(self) -> int:
        _, _, val = heappop(self.heap)
        self.numbers[val] += 1
        return val


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