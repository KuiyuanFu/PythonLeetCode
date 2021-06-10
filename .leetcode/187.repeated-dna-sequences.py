# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (41.92%)
# Likes:    1241
# Dislikes: 339
# Total Accepted:    212.1K
# Total Submissions: 505.1K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A',
# 'C', 'G', and 'T'.
#
#
# For example, "ACGAATTCCG" is a DNA sequence.
#
#
# When studying DNA, it is useful to identify repeated sequences within the
# DNA.
#
# Given a string s that represents a DNA sequence, return all the
# 10-letter-long sequences (substrings) that occur more than once in a DNA
# molecule. You may return the answer in any order.
#
#
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is either 'A', 'C', 'G', or 'T'.
#
#
#

# @lc tags=hash-table;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定序列，求指定长度重复出现的字符串。
# 直接字典。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        mem = defaultdict(int)
        size = 10
        for i in range(len(s) - size + 1):
            mem[s[i:i + size]] += 1
        result = []
        for d in mem.items():
            if d[1] > 1:
                result.append(d[0])
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"')
    print('Exception :')
    print('["AAAAACCCCC","CCCCCAAAAA"]')
    print('Output :')
    print(
        str(Solution().findRepeatedDnaSequences(
            "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "AAAAAAAAAAAAA"')
    print('Exception :')
    print('["AAAAAAAAAA"]')
    print('Output :')
    print(str(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA")))
    print()

    pass
# @lc main=end