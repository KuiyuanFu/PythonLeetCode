# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (69.67%)
# Likes:    2697
# Dislikes: 130
# Total Accepted:    174K
# Total Submissions: 246K
# Testcase Example:  '"a1b2"'
#
# Given a string s, we can transform every letter individually to be lowercase
# or uppercase to create another string.
#
# Return a list of all possible strings we could create. You can return the
# output in any order.
#
#
# Example 1:
#
#
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
#
#
# Example 2:
#
#
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
#
#
# Example 3:
#
#
# Input: s = "12345"
# Output: ["12345"]
#
#
# Example 4:
#
#
# Input: s = "0"
# Output: ["0"]
#
#
#
# Constraints:
#
#
# s will be a string with length between 1 and 12.
# s will consist only of letters or digits.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 转换成大小写不同格式。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return [
            ''.join(l) for l in \
                product(\
                    *[[c.upper(), c.lower()] if c.isalpha() else [c] for c in s]\
                        )
        ]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "a1b2"')
    print('Exception :')
    print('["a1b2","a1B2","A1b2","A1B2"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("a1b2")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "3z4"')
    print('Exception :')
    print('["3z4","3Z4"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("3z4")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "12345"')
    print('Exception :')
    print('["12345"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("12345")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "0"')
    print('Exception :')
    print('["0"]')
    print('Output :')
    print(str(Solution().letterCasePermutation("0")))
    print()

    pass
# @lc main=end