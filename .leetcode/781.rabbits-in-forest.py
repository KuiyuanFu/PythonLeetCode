# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#
# https://leetcode.com/problems/rabbits-in-forest/description/
#
# algorithms
# Medium (55.99%)
# Likes:    563
# Dislikes: 446
# Total Accepted:    32.1K
# Total Submissions: 57.5K
# Testcase Example:  '[1,1,2]'
#
# There is a forest with an unknown number of rabbits. We asked n rabbits "How
# many rabbits have the same color as you?" and collected the answers in an
# integer array answers where answers[i] is the answer of the i^th rabbit.
#
# Given the array answers, return the minimum number of rabbits that could be
# in the forest.
#
#
# Example 1:
#
#
# Input: answers = [1,1,2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit that answered "2" can't be red or the answers would be
# inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer
# into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that
# answered plus 2 that didn't.
#
#
# Example 2:
#
#
# Input: answers = [10,10,10]
# Output: 11
#
#
#
# Constraints:
#
#
# 1 <= answers.length <= 1000
# 0 <= answers[i] < 1000
#
#
#

# @lc tags=hash-table;string;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 深林里有兔子，求兔子数量，问n只兔子，多少与其颜色相同的兔子。
# 统计。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(int)
        for a in answers:
            d[a + 1] += 1
        res = 0
        for c in d:
            v = d[c]
            t = ((v - 1) // c + 1) * c
            res += t
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('answers = [1,1,2]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().numRabbits([1, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('answers = [10,10,10]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().numRabbits([10, 10, 10])))
    print()

    pass
# @lc main=end