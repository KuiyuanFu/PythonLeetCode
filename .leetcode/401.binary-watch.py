# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#
# https://leetcode.com/problems/binary-watch/description/
#
# algorithms
# Easy (49.16%)
# Likes:    795
# Dislikes: 1459
# Total Accepted:    100.2K
# Total Submissions: 203.2K
# Testcase Example:  '1'
#
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a
# zero or one, with the least significant bit on the right.
#
#
# For example, the below binary watch reads "4:51".
#
#
#
#
# Given an integer turnedOn which represents the number of LEDs that are
# currently on, return all possible times the watch could represent. You may
# return the answer in any order.
#
# The hour must not contain a leading zero.
#
#
# For example, "01:00" is not valid. It should be "1:00".
#
#
# The minute must be consist of two digits and may contain a leading
# zero.
#
#
# For example, "10:2" is not valid. It should be "10:02".
#
#
#
# Example 1:
# Input: turnedOn = 1
# Output:
# ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:
# Input: turnedOn = 9
# Output: []
#
#
# Constraints:
#
#
# 0 <= turnedOn <= 10
#
#
#

# @lc tags=backtracking;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二进制表，表上每个灯表示不同的时间，表的时间为所有灯相加。给定亮灯个数，求所有可能的时间。
# 直接遍历。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self) -> None:
        hours = [1, 2, 4, 8]
        hoursBuffer = defaultdict(list)
        hoursBuffer[0].append(0)
        hoursSum = sum(hours)
        if hoursSum < 12:
            hoursBuffer[4].append(hoursSum)
        for i in range(len(hours)):
            vi = hours[i]
            hoursBuffer[1].append(vi)
            if hoursSum - vi < 12:
                hoursBuffer[3].append(hoursSum - vi)
            for j in range(i + 1, len(hours)):
                vj = hours[j]
                if (vi + vj) < 12:
                    hoursBuffer[2].append(vi + vj)
                # if hoursSum - (vi + vj) < 24:
                #     hoursBuffer[3].append(hoursSum - (vi + vj))
                # for k in range(j + 1, len(hours)):
                #     vk = hours[k]
                #     if vi + vj + vk < 24:
                #         hoursBuffer[3].append(vi + vj + vk)
        self.hoursBuffer = hoursBuffer

        minutes = [1, 2, 4, 8, 16, 32]
        minutesBuffer = defaultdict(list)
        minutesBuffer[0].append(0)
        minutesSum = sum(minutes)
        if minutesSum < 60:
            minutesBuffer[6].append(minutesSum)
        for i in range(len(minutes)):
            vi = minutes[i]
            minutesBuffer[1].append(vi)
            if minutesSum - vi < 60:
                minutesBuffer[5].append(minutesSum - vi)
            for j in range(i + 1, len(minutes)):
                vj = minutes[j]
                minutesBuffer[2].append(vi + vj)
                if minutesSum - (vi + vj) < 60:
                    minutesBuffer[4].append(minutesSum - (vi + vj))
                for k in range(j + 1, len(minutes)):
                    vk = minutes[k]
                    if vi + vj + vk < 60:
                        minutesBuffer[3].append(vi + vj + vk)
                    # if minutesSum - (vi + vj + vk) < 60:
                    #     minutesBuffer[3].append(minutesSum - (vi + vj + vk))
        self.minutesBuffer = minutesBuffer

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = set()
        for i in range(turnedOn + 1):
            j = turnedOn - i
            hl = self.hoursBuffer[i]
            ml = self.minutesBuffer[j]
            for h in hl:
                for m in ml:
                    res.add(str(h) + ':' + str(m).zfill(2))
        return sorted(list(res))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().readBinaryWatch(1)))
    print(str(Solution().readBinaryWatch(2)))
    print(str(Solution().readBinaryWatch(3)))
    print(str(Solution().readBinaryWatch(4)))
    print(str(Solution().readBinaryWatch(5)))
    print(str(Solution().readBinaryWatch(6)))
    print(str(Solution().readBinaryWatch(7)))
    print(str(Solution().readBinaryWatch(8)))
    print(str(Solution().readBinaryWatch(9)))
    print('Example 1:')
    print('Input : ')
    print('turnedOn = 1')
    print('Exception :')
    print(
        '["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]'
    )
    print('Output :')
    print(str(Solution().readBinaryWatch(1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('turnedOn = 9')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().readBinaryWatch(9)))
    print()

    pass
# @lc main=end