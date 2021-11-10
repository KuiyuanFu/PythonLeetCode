# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (45.86%)
# Likes:    1071
# Dislikes: 1041
# Total Accepted:    139.5K
# Total Submissions: 304.4K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# Given a characters array letters that is sorted in non-decreasing order and a
# character target, return the smallest character in the array that is larger
# than target.
#
# Note that the letters wrap around.
#
#
# For example, if target == 'z' and letters == ['a', 'b'], the answer is
# 'a'.
#
#
#
# Example 1:
#
#
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
#
#
# Example 2:
#
#
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#
#
# Example 3:
#
#
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
#
#
# Example 4:
#
#
# Input: letters = ["c","f","j"], target = "g"
# Output: "j"
#
#
# Example 5:
#
#
# Input: letters = ["c","f","j"], target = "j"
# Output: "c"
#
#
#
# Constraints:
#
#
# 2 <= letters.length <= 10^4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.
#
#
#

# @lc tags=heap;depth-first-search;breadth-first-search;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target) % len(letters)]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('letters = ["c","f","j"], target = "a"')
    print('Exception :')
    print('"c"')
    print('Output :')
    print(str(Solution().nextGreatestLetter(["c", "f", "j"], "a")))
    print()

    print('Example 2:')
    print('Input : ')
    print('letters = ["c","f","j"], target = "c"')
    print('Exception :')
    print('"f"')
    print('Output :')
    print(str(Solution().nextGreatestLetter(["c", "f", "j"], "c")))
    print()

    print('Example 3:')
    print('Input : ')
    print('letters = ["c","f","j"], target = "d"')
    print('Exception :')
    print('"f"')
    print('Output :')
    print(str(Solution().nextGreatestLetter(["c", "f", "j"], "d")))
    print()

    print('Example 4:')
    print('Input : ')
    print('letters = ["c","f","j"], target = "g"')
    print('Exception :')
    print('"j"')
    print('Output :')
    print(str(Solution().nextGreatestLetter(["c", "f", "j"], "g")))
    print()

    print('Example 5:')
    print('Input : ')
    print('letters = ["c","f","j"], target = "j"')
    print('Exception :')
    print('"c"')
    print('Output :')
    print(str(Solution().nextGreatestLetter(["c", "f", "j"], "j")))
    print()

    pass
# @lc main=end