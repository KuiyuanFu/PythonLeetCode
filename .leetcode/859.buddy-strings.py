# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (28.76%)
# Likes:    1362
# Dislikes: 869
# Total Accepted:    115.7K
# Total Submissions: 402.2K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings s and goal, return true if you can swap two letters in s so
# the result is equal to goal, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such
# that i != j and swapping the characters at s[i] and s[j].
#
#
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
#
#
# Example 1:
#
#
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is
# equal to goal.
#
#
# Example 2:
#
#
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b',
# which results in "ba" != goal.
#
#
# Example 3:
#
#
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is
# equal to goal.
#
#
#
# Constraints:
#
#
# 1 <= s.length, goal.length <= 2 * 10^4
# s and goal consist of lowercase letters.
#
#
#

# @lc tags=design;queue

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        counts = [False] * 26
        f = False
        length = len(s)
        difIdies = []
        for i in range(length):
            if s[i] == goal[i]:
                if counts[ord(s[i]) - ord('a')]:
                    f = True
                else:
                    counts[ord(s[i]) - ord('a')] = True
            else:
                difIdies.append(i)
                if len(difIdies) == 2:
                    if not (s[difIdies[0]] == goal[difIdies[1]]
                            and s[difIdies[1]] == goal[difIdies[0]]):
                        return False
                elif len(difIdies) > 2:
                    return False
        if len(difIdies) == 1:
            return False
        if len(difIdies) == 0 and not f:
            return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ab", goal = "ba"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().buddyStrings("ab", "ba")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "ab", goal = "ab"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().buddyStrings("ab", "ab")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "aa", goal = "aa"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().buddyStrings("aa", "aa")))
    print()

    pass
# @lc main=end