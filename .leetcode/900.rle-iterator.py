# @lc app=leetcode id=900 lang=python3
#
# [900] RLE Iterator
#
# https://leetcode.com/problems/rle-iterator/description/
#
# algorithms
# Medium (58.70%)
# Likes:    521
# Dislikes: 144
# Total Accepted:    51.1K
# Total Submissions: 87.1K
# Testcase Example:  '["RLEIterator","next","next","next","next"]\n' +
# '[[[3,8,0,9,2,5]],[2],[1],[1],[2]]'
#
# We can use run-length encoding (i.e., RLE) to encode a sequence of integers.
# In a run-length encoded array of even length encoding (0-indexed), for all
# even i, encoding[i] tells us the number of times that the non-negative
# integer value encoding[i + 1] is repeated in the sequence.
#
#
# For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding =
# [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are also
# valid RLE of arr.
#
#
# Given a run-length encoded array, design an iterator that iterates through
# it.
#
# Implement the RLEIterator class:
#
#
# RLEIterator(int[] encoded) Initializes the object with the encoded array
# encoded.
# int next(int n) Exhausts the next n elements and returns the last element
# exhausted in this way. If there is no element left to exhaust, return -1
# instead.
#
#
#
# Example 1:
#
#
# Input
# ["RLEIterator", "next", "next", "next", "next"]
# [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
# Output
# [null, 8, 8, 5, -1]
#
# Explanation
# RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // This maps
# to the sequence [8,8,8,5,5].
# rLEIterator.next(2); // exhausts 2 terms of the sequence, returning 8. The
# remaining sequence is now [8, 5, 5].
# rLEIterator.next(1); // exhausts 1 term of the sequence, returning 8. The
# remaining sequence is now [5, 5].
# rLEIterator.next(1); // exhausts 1 term of the sequence, returning 5. The
# remaining sequence is now [5].
# rLEIterator.next(2); // exhausts 2 terms, returning -1. This is because the
# first term exhausted was 5,
# but the second term did not exist. Since the last term exhausted does not
# exist, we return -1.
#
#
#
# Constraints:
#
#
# 2 <= encoding.length <= 1000
# encoding.length is even.
# 0 <= encoding[i] <= 10^9
# 1 <= n <= 10^9
# At most 1000 calls will be made to next.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 长度编码。
# 直接迭代。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0
        self.length = len(self.encoding)

    def next(self, n: int) -> int:

        while self.idx < self.length and n > self.encoding[self.idx]:
            n -= self.encoding[self.idx]
            self.idx += 2

        if self.idx < self.length:
            self.encoding[self.idx] -= n
            return self.encoding[self.idx + 1]
        else:
            return -1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end