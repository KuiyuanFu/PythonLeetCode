# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (27.44%)
# Likes:    5590
# Dislikes: 841
# Total Accepted:    527.3K
# Total Submissions: 1.9M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where:
#
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
#
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
#
#
# Example 5:
#
#
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
#
#
#

#
#

# @lc tags=string;dynamic-programming;backtracking

# @lc imports=start
from subprocess import STARTF_USESHOWWINDOW
from imports import *

# @lc imports=end

# @lc idea=start
#
# 正则表达式匹配。
# 非确定性有限状态自动机。
#
# @lc idea=end

# @lc group=nfa

# @lc rank=10


# @lc code=start
class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        length = len(p)
        #          null  self    next
        states = [[False, None, None]]

        idx = 0
        while idx < length:
            preState = states[-1]
            newState = [False, None, None]

            preState[2] = p[idx]

            if idx + 1 < length and p[idx + 1] == '*':
                preState[0] = True
                newState[1] = p[idx]
                idx += 1

            states.append(newState)
            idx += 1

        def addState(newStates: set, newStateIdx: int):

            while newStateIdx is not None and newStateIdx not in newStates:
                newStates.add(newStateIdx)
                newStateIdx = newStateIdx + 1 if states[newStateIdx][
                    0] else None

        nowStates = set()
        addState(nowStates, 0)

        for c in s:

            newStates = set()

            for stateIdx in nowStates:

                state = states[stateIdx]

                if state[1] == '.' or state[1] == c:
                    # self
                    addState(newStates, stateIdx)

                if state[2] == '.' or state[2] == c:
                    # next
                    addState(newStates, stateIdx + 1)
            nowStates = newStates
            pass

        return len(states) - 1 in nowStates


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aa", p = "a"')
    print('Output :')
    print(str(Solution().isMatch("aa", "a")))
    print('Exception :')
    print('false')
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aa", p = "a*"')
    print('Output :')
    print(str(Solution().isMatch("aa", "a*")))
    print('Exception :')
    print('true')
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "ab", p = ".*"')
    print('Output :')
    print(str(Solution().isMatch("ab", ".*")))
    print('Exception :')
    print('true')
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "aab", p = "c*a*b"')
    print('Output :')
    print(str(Solution().isMatch("aab", "c*a*b")))
    print('Exception :')
    print('true')
    print()

    print('Example 5:')
    print('Input : ')
    print('s = "mississippi", p = "mis*is*p*."')
    print('Output :')
    print(str(Solution().isMatch("mississippi", "mis*is*p*.")))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end