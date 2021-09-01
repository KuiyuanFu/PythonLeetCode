# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
# https://leetcode.com/problems/string-compression/description/
#
# algorithms
# Medium (45.55%)
# Likes:    1536
# Dislikes: 3615
# Total Accepted:    194.8K
# Total Submissions: 426.6K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# Given an array of characters chars, compress it using the following
# algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating
# characters in chars:
#
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
#
#
# The compressed string s should not be returned separately, but instead, be
# stored in the input character array chars. Note that group lengths that are
# 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the
# array.
# You must write an algorithm that uses only constant extra space.
#
# Example 1:
#
#
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to
# "a2b2c3".
#
#
# Example 2:
#
#
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a
# single character.
#
#
# Example 3:
#
#
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to
# "ab12".
#
# Example 4:
#
#
# Input: chars = ["a","a","a","b","b","a","a"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","3","b","2","a","2"].
# Explanation: The groups are "aaa", "bb", and "aa". This compresses to
# "a3b2a2". Note that each group is independent even if two groups have the
# same character.
#
#
#
# Constraints:
#
#
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or
# symbol.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 压缩字符串。
# 双指针。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        l, n = 0, 0
        cp = ' '
        length = len(chars)
        for c in chars:
            if c != cp:
                if n > 1:
                    s = list(str(n))
                    chars[l:l + len(s)] = s[:]
                    l += len(s)
                chars[l] = c
                l += 1
                cp = c
                n = 1
            else:
                n += 1
        if n > 1:
            s = list(str(n))
            chars[l:l + len(s)] = s[:]
            l += len(s)
        return l
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('chars = ["a","a","b","b","c","c","c"]')
    print('Exception :')
    print(
        'Return 6, and the first 6 characters of the input array should be:["a","2","b","2","c","3"]'
    )
    print('Output :')
    print(str(Solution().compress(["a", "a", "b", "b", "c", "c", "c"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('chars = ["a"]')
    print('Exception :')
    print(
        'Return 1, and the first character of the input array should be: ["a"]'
    )
    print('Output :')
    print(str(Solution().compress(["a"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]')
    print('Exception :')
    print(
        'Return 4, and the first 4 characters of the input array should be:["a","b","1","2"].'
    )
    print('Output :')
    print(
        str(Solution().compress(
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
             "b"])))
    print()

    print('Example 4:')
    print('Input : ')
    print('chars = ["a","a","a","b","b","a","a"]')
    print('Exception :')
    print(
        'Return 6, and the first 6 characters of the input array should be:["a","3","b","2","a","2"].'
    )
    print('Output :')
    print(str(Solution().compress(["a", "a", "a", "b", "b", "a", "a"])))
    print()

    pass
# @lc main=end