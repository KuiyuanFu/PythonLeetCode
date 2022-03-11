# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#
# https://leetcode.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (45.00%)
# Likes:    748
# Dislikes: 165
# Total Accepted:    48.6K
# Total Submissions: 107.9K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# Two strings X and Y are similar if we can swap two letters (in different
# positions) of X, so that it equals Y. Also two strings X and Y are similar if
# they are equal.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to "tars",
# "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats",
# "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group
# even though they are not similar.  Formally, each group is such that a word
# is in the group if and only if it is similar to at least one other word in
# the group.
#
# We are given a list strs of strings where every string in strs is an anagram
# of every other string in strs. How many groups are there?
#
#
# Example 1:
#
#
# Input: strs = ["tars","rats","arts","star"]
# Output: 2
#
#
# Example 2:
#
#
# Input: strs = ["omv","ovm"]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 300
# 1 <= strs[i].length <= 300
# strs[i] consists of lowercase letters only.
# All words in strs have the same length and are anagrams of each other.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from logging.config import dictConfig
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将相似的分成一组，问多少组。
# 图，直接判断相似，后遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        length = len(strs)
        sLength = len(strs[0])
        adjoins = [[] for _ in range(length)]
        for i in range(length):
            for j in range(i):
                si = strs[i]
                sj = strs[j]

                diffCount = 0
                c1, c2 = None, None

                for k in range(sLength):
                    if si[k] != sj[k]:
                        diffCount += 1
                        if diffCount == 1:
                            c1, c2 = si[k], sj[k]
                        elif diffCount == 2:
                            if c1 != sj[k] or c2 != si[k]:
                                diffCount += 1
                                break
                        else:
                            break
                if diffCount == 0 or diffCount == 2:

                    adjoins[i].append(j)
                    adjoins[j].append(i)

        res = 0

        visited = [True] * length

        for i in range(length):
            if visited[i]:
                res += 1
                s = [i]
                while len(s) > 0:
                    n = s.pop()
                    if visited[n]:
                        visited[n] = False
                        for m in adjoins[n]:
                            s.append(m)

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["tars","rats","arts","star"]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numSimilarGroups(["tars", "rats", "arts", "star"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = ["omv","ovm"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numSimilarGroups(["omv", "ovm"])))
    print()

    pass
# @lc main=end