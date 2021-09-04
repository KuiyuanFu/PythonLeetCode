# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (65.64%)
# Likes:    2791
# Dislikes: 157
# Total Accepted:    279.3K
# Total Submissions: 425.5K
# Testcase Example:  '"tree"'
#
# Given a string s, sort it in decreasing order based on the frequency of
# characters, and return the sorted string.
#
#
# Example 1:
#
#
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
#
#
# Example 2:
#
#
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid
# answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
# Example 3:
#
#
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^5
# s consists of English letters and digits.
#
#
#

# @lc tags=hash-table;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 按照字符出现频率排序。
# 字典统计个数，排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        l = [(-d[k], k) for k in d.keys()]
        l.sort()
        rs = [k * (-n) for n, k in l]
        return ''.join(rs)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "tree"')
    print('Exception :')
    print('"eert"')
    print('Output :')
    print(str(Solution().frequencySort("tree")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "cccaaa"')
    print('Exception :')
    print('"aaaccc"')
    print('Output :')
    print(str(Solution().frequencySort("cccaaa")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "Aabb"')
    print('Exception :')
    print('"bbAa"')
    print('Output :')
    print(str(Solution().frequencySort("Aabb")))
    print()

    pass
# @lc main=end