# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#
# https://leetcode.com/problems/word-subsets/description/
#
# algorithms
# Medium (52.68%)
# Likes:    962
# Dislikes: 126
# Total Accepted:    50.3K
# Total Submissions: 95.6K
# Testcase Example:  '["amazon","apple","facebook","google","leetcode"]\n["e","o"]'
#
# You are given two string arrays words1 and words2.
#
# A string b is a subset of string a if every letter in b occurs in a including
# multiplicity.
#
#
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
#
#
# A string a from words1 is universal if for every string b in words2, b is a
# subset of a.
#
# Return an array of all the universal strings in words1. You may return the
# answer in any order.
#
#
# Example 1:
#
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
# ["e","o"]
# Output: ["facebook","google","leetcode"]
#
#
# Example 2:
#
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
# ["l","e"]
# Output: ["apple","google","leetcode"]
#
#
#
# Constraints:
#
#
# 1 <= words1.length, words2.length <= 10^4
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters.
# All the strings of words1 are unique.
#
#
#

# @lc tags=stack

# @lc imports=start
from ast import Return
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个字符串数组，在第一个中找出，是第二个中所有元素的超集的元素。
# 统计字符串字符个数，取最大值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def generateDict():
            d = defaultdict(int)
            for w in words2:
                for k, v in Counter(w).items():
                    d[k] = max(d[k], v)
            return d

        d = generateDict()

        def valid(w):
            c = Counter(w)
            for k in d:

                if c[k] < d[k]:
                    return False
            return True

        return list(filter(valid, words1))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'words1 = ["amazon","apple","facebook","google","leetcode"], words2 =["e","o"]'
    )
    print('Exception :')
    print('["facebook","google","leetcode"]')
    print('Output :')
    print(
        str(Solution().wordSubsets(
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "o"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'words1 = ["amazon","apple","facebook","google","leetcode"], words2 =["l","e"]'
    )
    print('Exception :')
    print('["apple","google","leetcode"]')
    print('Output :')
    print(
        str(Solution().wordSubsets(
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["l", "e"])))
    print()

    pass
# @lc main=end