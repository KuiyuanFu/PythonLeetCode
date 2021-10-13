# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#
# https://leetcode.com/problems/bulb-switcher-ii/description/
#
# algorithms
# Medium (50.85%)
# Likes:    3
# Dislikes: 9
# Total Accepted:    15.5K
# Total Submissions: 30.4K
# Testcase Example:  '1\n1'
#
# There is a room with n bulbs labeled from 1 to n that all are turned on
# initially, and four buttons on the wall. Each of the four buttons has a
# different functionality where:
#
#
# Button 1: Flips the status of all the bulbs.
# Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4,
# ...).
# Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3,
# ...).
# Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k =
# 0, 1, 2, ... (i.e., 1, 4, 7, 10, ...).
#
#
# You must make exactly presses button presses in total. For each press, you
# may pick any of the four buttons to press.
#
# Given the two integers n and presses, return the number of different possible
# statuses after performing all presses button presses.
#
#
# Example 1:
#
#
# Input: n = 1, presses = 1
# Output: 2
# Explanation: Status can be:
# - [off] by pressing button 1
# - [on] by pressing button 2
#
#
# Example 2:
#
#
# Input: n = 2, presses = 1
# Output: 3
# Explanation: Status can be:
# - [off, off] by pressing button 1
# - [on, off] by pressing button 2
# - [off, on] by pressing button 3
#
#
# Example 3:
#
#
# Input: n = 3, presses = 1
# Output: 4
# Explanation: Status can be:
# - [off, off, off] by pressing button 1
# - [off, on, off] by pressing button 2
# - [on, off, on] by pressing button 3
# - [off, on, on] by pressing button 4
#
#
# Example 4:
#
#
# Input: n = 1, presses = 0
# Output: 1
# Explanation: Status can only be [on] since you cannot press any of the
# buttons.
#
#
# Example 5:
#
#
# Input: n = 1, presses = 2
# Output: 2
# Explanation: Status can be:
# - [off] by pressing button 1 then button 1 again
# - [on] by pressing button 1 then button 2
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
# 0 <= presses <= 1000
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 开灯，四个按钮，依次控制所有、奇数、偶数、模3的灯。按确定的次数，会有多少种结果。
# 一共四个信号，1，2，3，4.分别由奇数模三、偶数、奇数、偶数模三。
# 指定每个信号可以操作的信号位。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def flipLights(self, n: int, presses: int) -> int:

        signals = [0b111111, 0b101010, 0b010101, 0b001001]
        n = min(n, 6)
        signals = list(set([s & (2**n - 1) for s in signals]))
        s = set([0])
        for _ in range(presses):
            sn = set()
            for signal in signals:
                for b in s:
                    sn.add(signal ^ b)
            if len(sn) == len(s):
                break
            s = sn
        return len(s)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1, presses = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().flipLights(1, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2, presses = 1')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().flipLights(2, 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 3, presses = 1')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().flipLights(3, 1)))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 1, presses = 0')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().flipLights(1, 0)))
    print()

    print('Example 5:')
    print('Input : ')
    print('n = 1, presses = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().flipLights(1, 2)))
    print()

    pass
# @lc main=end