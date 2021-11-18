# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#
# https://leetcode.com/problems/pyramid-transition-matrix/description/
#
# algorithms
# Medium (55.92%)
# Likes:    422
# Dislikes: 410
# Total Accepted:    25.9K
# Total Submissions: 46.7K
# Testcase Example:  '"BCD"\n["BCC","CDE","CEA","FFF"]'
#
# You are stacking blocks to form a pyramid. Each block has a color, which is
# represented by a single letter. Each row of blocks contains one less block
# than the row beneath it and is centered on top.
#
# To make the pyramid aesthetically pleasing, there are only specific
# triangular patterns that are allowed. A triangular pattern consists of a
# single block stacked on top of two blocks. The patterns are given as a list
# of three-letter strings allowed, where the first two characters of a pattern
# represent the left and right bottom blocks respectively, and the third
# character is the top block.
#
#
# For example, "ABC" represents a triangular pattern with a 'C' block stacked
# on top of an 'A' (left) and 'B' (right) block. Note that this is different
# from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
#
#
# You start with a bottom row of blocks bottom, given as a single string, that
# you must use as the base of the pyramid.
#
# Given bottom and allowed, return true if you can build the pyramid all the
# way to the top such that every triangular pattern in the pyramid is in
# allowed, or false otherwise.
#
#
# Example 1:
#
#
# Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
# Output: true
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 3), we can build "CE" on level 2 and then
# build "E" on level 1.
# There are three triangular patterns in the pyramid, which are "BCC", "CDE",
# and "CEA". All are allowed.
#
#
# Example 2:
#
#
# Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
# Output: false
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 4), there are multiple ways to build level 3,
# but trying all the possibilites, you will get always stuck before building
# level 1.
#
#
#
# Constraints:
#
#
# 2 <= bottom.length <= 6
# 0 <= allowed.length <= 216
# allowed[i].length == 3
# The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E',
# 'F'}.
# All the values of allowed are unique.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 搭金字塔，下一层的两个字符决定了上一层这个位置可能的值。
# 遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        allowedDict = defaultdict(list)
        for s in allowed:
            b, u = s[:2], s[2]
            if b not in allowedDict:
                allowedDict[b] = []
            allowedDict[b].append(u)

        s = set([bottom])
        while s:
            button = s.pop()
            if len(button) == 1:
                return True
            buttonLists = [
                allowedDict[button[i:i + 2]] for i in range(len(button) - 1)
            ]
            f = False
            for us in buttonLists:
                if len(us) == 0:
                    f = True
                    break
            if f:
                continue

            ls = product(*buttonLists)

            for t in ls:
                s.add(''.join(t))

        return False
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().pyramidTransition("AAAA",
                                         ["AAB", "AAC", "BCD", "BBE", "DEF"])))
    print()
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().pyramidTransition("CCC", [
            "CBB", "ACB", "ABD", "CDB", "BDC", "CBC", "DBA", "DBB", "CAB",
            "BCB", "BCC", "BAA", "CCD", "BDD", "DDD", "CCA", "CAA", "CCC",
            "CCB"
        ])))
    print()
    print()
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().pyramidTransition("ABBBBA", [
            "ACA", "ACF", "ACE", "ACD", "ABA", "ABF", "ABE", "ABD", "FCA",
            "FCF", "FCE", "FCD", "FBA", "FBF", "FBE", "FBD", "ECA", "ECF",
            "ECE", "ECD", "EBA", "EBF", "EBE", "EBD", "DCA", "DCF", "DCE",
            "DCD", "DBA", "DBF", "DBE", "DBD", "CAA", "CAF", "CAE", "CAD",
            "CFA", "CFF", "CFE", "CFD", "CEA", "CEF", "CEE", "CED", "CDA",
            "CDF", "CDE", "CDD", "BAA", "BAF", "BAE", "BAD", "BFA", "BFF",
            "BFE", "BFD", "BEA", "BEF", "BEE", "BED", "BDA", "BDF", "BDE",
            "BDD", "CCA", "CCF", "CCE", "CCD", "CBA", "CBF", "CBE", "CBD",
            "BCA", "BCF", "BCE", "BCD", "BBA", "BBF", "BBE", "BBD", "CCC",
            "CCB", "CBC", "CBB", "BCC", "BCB", "BBC", "BBB"
        ])))
    print()
    pass
# @lc main=end
