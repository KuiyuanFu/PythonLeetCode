# @lc app=leetcode id=753 lang=python3
#
# [753] Cracking the Safe
#
# https://leetcode.com/problems/cracking-the-safe/description/
#
# algorithms
# Hard (53.29%)
# Likes:    93
# Dislikes: 13
# Total Accepted:    41.9K
# Total Submissions: 77.8K
# Testcase Example:  '1\n2'
#
# There is a safe protected by a password. The password is a sequence of n
# digits where each digit can be in the range [0, k - 1].
#
# The safe has a peculiar way of checking the password. When you enter in a
# sequence, it checks the most recent n digits that were entered each time you
# type a digit.
#
#
# For example, the correct password is "345" and you enter in
# "012345":
#
#
# After typing 0, the most recent 3 digits is "0", which is incorrect.
# After typing 1, the most recent 3 digits is "01", which is incorrect.
# After typing 2, the most recent 3 digits is "012", which is
# incorrect.
# After typing 3, the most recent 3 digits is "123", which is
# incorrect.
# After typing 4, the most recent 3 digits is "234", which is
# incorrect.
# After typing 5, the most recent 3 digits is "345", which is correct and the
# safe unlocks.
#
#
#
#
# Return any string of minimum length that will unlock the safe at some point
# of entering it.
#
#
# Example 1:
#
#
# Input: n = 1, k = 2
# Output: "10"
# Explanation: The password is a single digit, so enter each digit. "01" would
# also unlock the safe.
#
#
# Example 2:
#
#
# Input: n = 2, k = 2
# Output: "01100"
# Explanation: For each possible password:
# - "00" is typed in starting from the 4^th digit.
# - "01" is typed in starting from the 1^st digit.
# - "10" is typed in starting from the 3^rd digit.
# - "11" is typed in starting from the 2^nd digit.
# Thus "01100" will unlock the safe. "01100", "10011", and "11001" would also
# unlock the safe.
#
#
#
# Constraints:
#
#
# 1 <= n <= 4
# 1 <= k <= 10
# 1 <= k^n <= 4096
#
#
#

# @lc tags=breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 生成一个最小序列，使所有密码都出现一次。
# 直接深度优先。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def crackSafe(self, n: int, k: int) -> str:

        visited = set()
        visited.add('0' * n)
        targetCount = k**n
        res = ['0'] * n

        cl = [str(i) for i in range(k)]

        def recur():
            if len(visited) == targetCount:
                return True

            for c in cl:
                res.append(c)
                key = ''.join(res[-n:])
                if key not in visited:
                    visited.add(key)
                    if recur():
                        return True
                    visited.remove(key)
                res.pop()
            return False

        recur()

        return ''.join(res)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1, k = 2')
    print('Exception :')
    print('"10"')
    print('Output :')
    print(str(Solution().crackSafe(1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2, k = 2')
    print('Exception :')
    print('"01100"')
    print('Output :')
    print(str(Solution().crackSafe(2, 2)))
    print()

    pass
# @lc main=end