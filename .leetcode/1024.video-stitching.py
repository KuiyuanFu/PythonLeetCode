# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#
# https://leetcode.com/problems/video-stitching/description/
#
# algorithms
# Medium (50.44%)
# Likes:    1398
# Dislikes: 50
# Total Accepted:    53.3K
# Total Submissions: 105.7K
# Testcase Example:  '[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]\n10'
#
# You are given a series of video clips from a sporting event that lasted time
# seconds. These video clips can be overlapping with each other and have
# varying lengths.
#
# Each video clip is described by an array clips where clips[i] = [starti,
# endi] indicates that the ith clip started at starti and ended at endi.
#
# We can cut these clips into segments freely.
#
#
# For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3,
# 7].
#
#
# Return the minimum number of clips needed so that we can cut the clips into
# segments that cover the entire sporting event [0, time]. If the task is
# impossible, return -1.
#
#
# Example 1:
#
#
# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
# Output: 3
# Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event
# [0, 10].
#
#
# Example 2:
#
#
# Input: clips = [[0,1],[1,2]], time = 5
# Output: -1
# Explanation: We cannot cover [0,5] with only [0,1] and [1,2].
#
#
# Example 3:
#
#
# Input: clips =
# [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
# time = 9
# Output: 3
# Explanation: We can take clips [0,4], [4,7], and [6,9].
#
#
#
# Constraints:
#
#
# 1 <= clips.length <= 100
# 0 <= starti <= endi <= 100
# 1 <= time <= 100
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from pydoc import cli
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定时间区间序列，求最少的个数可以覆盖给定区间。
# 找当前最长的覆盖序列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        res = 0
        n = 0
        heapify(clips)
        while True:
            t = 0
            while len(clips) > 0 and clips[0][0] <= n:
                t = max(t, heappop(clips)[1])

            if t == 0:
                return -1
            n = t
            res += 1
            if n >= time:
                return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().videoStitching(
            [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('clips = [[0,1],[1,2]], time = 5')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().videoStitching([[0, 1], [1, 2]], 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'clips =[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],time = 9'
    )
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().videoStitching(
            [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3],
             [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]],
            9)))
    print()

    pass
# @lc main=end