# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
# https://leetcode.com/problems/dota2-senate/description/
#
# algorithms
# Medium (39.73%)
# Likes:    370
# Dislikes: 279
# Total Accepted:    16.9K
# Total Submissions: 42.4K
# Testcase Example:  '"RD"'
#
# In the world of Dota2, there are two parties: the Radiant and the Dire.
#
# The Dota2 senate consists of senators coming from two parties. Now the Senate
# wants to decide on a change in the Dota2 game. The voting for this change is
# a round-based procedure. In each round, each senator can exercise one of the
# two rights:
#
#
# Ban one senator's right: A senator can make another senator lose all his
# rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have
# rights to vote are all from the same party, he can announce the victory and
# decide on the change in the game.
#
#
# Given a string senate representing each senator's party belonging. The
# character 'R' and 'D' represent the Radiant party and the Dire party. Then if
# there are n senators, the size of the given string will be n.
#
# The round-based procedure starts from the first senator to the last senator
# in the given order. This procedure will last until the end of voting. All the
# senators who have lost their rights will be skipped during the procedure.
#
# Suppose every senator is smart enough and will play the best strategy for his
# own party. Predict which party will finally announce the victory and change
# the Dota2 game. The output should be "Radiant" or "Dire".
#
#
# Example 1:
#
#
# Input: senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's
# right in round 1.
# And the second senator can't exercise any rights anymore since his right has
# been banned.
# And in round 2, the first senator can just announce the victory since he is
# the only guy in the senate who can vote.
#
#
# Example 2:
#
#
# Input: senate = "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's
# right in round 1.
# And the second senator can't exercise any rights anymore since his right has
# been banned.
# And the third senator comes from Dire and he can ban the first senator's
# right in round 1.
# And in round 2, the third senator can just announce the victory since he is
# the only guy in the senate who can vote.
#
#
#
# Constraints:
#
#
# n == senate.length
# 1 <= n <= 10^4
# senate[i] is either 'R' or 'D'.
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 表决。队列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rr, dr = 0, 0
        while True:
            senateN = []
            r = senate.count('R')
            d = len(senate) - r
            for c in senate:
                if c == 'R':
                    # no right
                    if rr > 0:
                        rr -= 1
                    # exe right
                    else:
                        if d == 0:
                            return "Radiant"
                        else:
                            dr += 1
                            d -= 1

                        senateN.append('R')

                else:
                    if dr > 0:
                        dr -= 1
                    else:
                        if r == 0:
                            return "Dire"
                        else:
                            rr += 1
                            r -= 1

                        senateN.append('D')
            senate = senateN


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('senate = "RD"')
    print('Exception :')
    print('"Radiant"')
    print('Output :')
    print(str(Solution().predictPartyVictory("RD")))
    print()

    print('Example 2:')
    print('Input : ')
    print('senate = "RDD"')
    print('Exception :')
    print('"Dire"')
    print('Output :')
    print(str(Solution().predictPartyVictory("RDD")))
    print()
    print(str(Solution().predictPartyVictory("RRDDDDDDDRRDRRDDRRRR")))
    print(str(Solution().predictPartyVictory("DDRRR")))
    pass
# @lc main=end