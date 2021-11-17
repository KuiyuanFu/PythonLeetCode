# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#
# https://leetcode.com/problems/open-the-lock/description/
#
# algorithms
# Medium (54.83%)
# Likes:    2362
# Dislikes: 81
# Total Accepted:    136.3K
# Total Submissions: 247.6K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# You have a lock in front of you with 4 circular wheels. Each wheel has 10
# slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can
# rotate freely and wrap around: for example we can turn '9' to be '0', or '0'
# to be '9'. Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4
# wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any
# of these codes, the wheels of the lock will stop turning and you will be
# unable to open it.
#
# Given a target representing the value of the wheels that will unlock the
# lock, return the minimum total number of turns required to open the lock, or
# -1 if it is impossible.
#
#
# Example 1:
#
#
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" ->
# "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202"
# would be invalid,
# because the wheels of the lock become stuck after the display becomes the
# dead end "0102".
#
#
# Example 2:
#
#
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
#
#
# Example 3:
#
#
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
#
#
# Example 4:
#
#
# Input: deadends = ["0000"], target = "8888"
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 锁，每次移动一位，不能达到一些值。
# 广度优先遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for dead in deadends:
            visited.add(int(dead))
        target = int(target)

        s = set()
        if 0 not in visited:
            s.add(0)
        i = 0
        while s:

            if target in s:
                return i
            i += 1

            sn = set()

            for n in s:
                if n in visited:
                    continue
                visited.add(n)
                n1, n2, n3, n4 = n // 1000, (n // 100) % 10, (n //
                                                              10) % 10, n % 10
                sn.add(((n1 + 1) % 10) * 1000 + n2 * 100 + n3 * 10 + n4)
                sn.add(((n1 + 9) % 10) * 1000 + n2 * 100 + n3 * 10 + n4)
                sn.add(n1 * 1000 + ((n2 + 1) % 10) * 100 + n3 * 10 + n4)
                sn.add(n1 * 1000 + ((n2 + 9) % 10) * 100 + n3 * 10 + n4)
                sn.add(n1 * 1000 + n2 * 100 + ((n3 + 1) % 10) * 10 + n4)
                sn.add(n1 * 1000 + n2 * 100 + ((n3 + 9) % 10) * 10 + n4)
                sn.add(n1 * 1000 + n2 * 100 + n3 * 10 + ((n4 + 1) % 10))
                sn.add(n1 * 1000 + n2 * 100 + n3 * 10 + ((n4 + 9) % 10))
            s = sn
        return -1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('deadends = ["0201","0101","0102","1212","2002"], target = "0202"')
    print('Exception :')
    print('6')
    print('Output :')
    print(
        str(Solution().openLock(["0201", "0101", "0102", "1212", "2002"],
                                "0202")))
    print()

    print('Example 2:')
    print('Input : ')
    print('deadends = ["8888"], target = "0009"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().openLock(["8888"], "0009")))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],target = "8888"'
    )
    print('Exception :')
    print('-1')
    print('Output :')
    print(
        str(Solution().openLock(
            ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
            "8888")))
    print()

    print('Example 4:')
    print('Input : ')
    print('deadends = ["0000"], target = "8888"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().openLock(["0000"], "8888")))
    print()

    pass
# @lc main=end