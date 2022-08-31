# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
# https://leetcode.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (67.62%)
# Likes:    3740
# Dislikes: 64
# Total Accepted:    185.3K
# Total Submissions: 274.1K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# Given two integer arrays pushed and popped each with distinct values, return
# true if this could have been the result of a sequence of push and pop
# operations on an initially empty stack, or false otherwise.
#
#
# Example 1:
#
#
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
#
# Example 2:
#
#
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#
#
#
# Constraints:
#
#
# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.
#
#
#

# @lc tags=math;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个压入序列和弹出序列，判断是否栈成立。
# 直接模拟。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:

        s = []
        idx = 0
        length = len(pushed)
        for n in popped:
            if len(s) == 0 or s[-1] != n:

                while idx <= length:
                    if idx == length:
                        return False
                    p = pushed[idx]
                    idx += 1
                    if p == n:
                        break
                    else:
                        s.append(p)

            else:
                s.pop()
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('pushed = [1,2,3,4,5], popped = [4,5,3,2,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().validateStackSequences([1, 2, 3, 4, 5],
                                              [4, 5, 3, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('pushed = [1,2,3,4,5], popped = [4,3,5,1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().validateStackSequences([1, 2, 3, 4, 5],
                                              [4, 3, 5, 1, 2])))
    print()

    pass
# @lc main=end