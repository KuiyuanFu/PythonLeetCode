# @lc app=leetcode id=1023 lang=python3
#
# [1023] Camelcase Matching
#
# https://leetcode.com/problems/camelcase-matching/description/
#
# algorithms
# Medium (60.09%)
# Likes:    672
# Dislikes: 246
# Total Accepted:    35.9K
# Total Submissions: 59.8K
# Testcase Example:  '["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]\n"FB"'
#
# Given an array of strings queries and a string pattern, return a boolean
# array answer where answer[i] is true if queries[i] matches pattern, and false
# otherwise.
#
# A query word queries[i] matches pattern if you can insert lowercase English
# letters pattern so that it equals the query. You may insert each character at
# any position and you may not insert any characters.
#
#
# Example 1:
#
#
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FB"
# Output: [true,false,true,true,false]
# Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
#
#
# Example 2:
#
#
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBa"
# Output: [true,false,true,false,false]
# Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
#
#
# Example 3:
#
#
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBaT"
# Output: [false,true,false,false,false]
# Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r"
# + "T" + "est".
#
#
#
# Constraints:
#
#
# 1 <= pattern.length, queries.length <= 100
# 1 <= queries[i].length <= 100
# queries[i] and pattern consist of English letters.
#
#
#

# @lc tags=hash-table;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断字符是否匹配
# 插入
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def match(s: str):
            ti = 0
            for c in s:
                if ti == len(pattern):
                    if c.lower() != c:
                        return False
                else:
                    if c == pattern[ti]:
                        ti += 1
                    elif c.upper() == c:
                        return False
            return ti == len(pattern)

        return list(map(match, queries))

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'queries =["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern ="FB"'
    )
    print('Exception :')
    print('[true,false,true,true,false]')
    print('Output :')
    print(
        str(Solution().camelMatch([
            "FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"
        ], "FB")))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'queries =["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern ="FoBa"'
    )
    print('Exception :')
    print('[true,false,true,false,false]')
    print('Output :')
    print(
        str(Solution().camelMatch([
            "FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"
        ], "FoBa")))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'queries =["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern ="FoBaT"'
    )
    print('Exception :')
    print('[false,true,false,false,false]')
    print('Output :')
    print(
        str(Solution().camelMatch([
            "FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"
        ], "FoBaT")))
    print()

    pass
# @lc main=end