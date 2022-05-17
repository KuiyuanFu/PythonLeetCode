# @lc app=leetcode id=920 lang=python3
#
# [920] Number of Music Playlists
#
# https://leetcode.com/problems/number-of-music-playlists/description/
#
# algorithms
# Hard (49.71%)
# Likes:    740
# Dislikes: 71
# Total Accepted:    19.2K
# Total Submissions: 38.4K
# Testcase Example:  '3\n3\n1'
#
# Your music player contains n different songs. You want to listen to goal
# songs (not necessarily different) during your trip. To avoid boredom, you
# will create a playlist so that:
#
#
# Every song is played at least once.
# A song can only be played again only if k other songs have been played.
#
#
# Given n, goal, and k, return the number of possible playlists that you can
# create. Since the answer can be very large, return it modulo 10^9 + 7.
#
# Example 1:
#
#
# Input: n = 3, goal = 3, k = 1
# Output: 6
# Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3],
# [2, 3, 1], [3, 1, 2], and [3, 2, 1].
#
#
# Example 2:
#
#
# Input: n = 2, goal = 3, k = 0
# Output: 6
# Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1],
# [2, 2, 1], [2, 1, 2], and [1, 2, 2].
#
#
# Example 3:
#
#
# Input: n = 2, goal = 3, k = 1
# Output: 2
# Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
#
#
#
# Constraints:
#
#
# 0 <= k < n <= goal <= 100
#
#
#

# @lc tags=hash-table

# @lc imports=start
from functools import reduce
import math
from attrs import asdict
from imports import *

# @lc imports=end

# @lc idea=start
#
# 音乐播放列表数量，要求重复出现的同一首歌之间必须间隔k首其他歌曲。且每首歌必须出现至少一次。
# 动态规划，记录不同歌曲数量在不同长度可以形成的歌单数目。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        length = n - k + 1
        l1 = length - 1
        dp = [0] * length
        dp[0] = math.perm(n, k)
        for _ in range(k, goal):
            dpn = [0] * length

            for idx in range(length - 1):
                dpn[idx] += dp[idx] * idx
                dpn[idx + 1] += dp[idx] * (n - k - idx)
            dpn[l1] += dp[l1] * (l1)
            dp = dpn

        return dp[-1] % 1000000007


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3, goal = 3, k = 1')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().numMusicPlaylists(3, 3, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2, goal = 3, k = 0')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().numMusicPlaylists(2, 3, 0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 2, goal = 3, k = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numMusicPlaylists(2, 3, 1)))
    print()

    pass
# @lc main=end