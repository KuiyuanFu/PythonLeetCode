# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (28.25%)
# Likes:    10060
# Dislikes: 1037
# Total Accepted:    1.3M
# Total Submissions: 4.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个整形数组，返回所有三元组，满足和为0。由于要求不能重复，需要有重复校验。最简单就是三重循环，这样复杂度太高了。由于是三个数，所以时间复杂度不可能太低。
# 这样先使用字典降重，使每个数最多为三个。之后使用字符串形式为两数之和确定一个唯一标识。最后，再次遍历，确定和是否等于0，此时检查是否使用了相同元素。
# 效率很低，很差，应该使用双指针。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 每一个数最多三个
        dic = {}
        for n in nums:
            if not dic.__contains__(n):
                dic[n] = 0
            if dic[n] < 3:
                dic[n] += 1
        nums = []
        for i in list(dic.keys()):
            nums += [i] * dic[i]

        # 存储两个值的和，并用字符串检查重复
        self.nums = nums
        sumToString = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n = nums[i] + nums[j]
                if not sumToString.__contains__(n):
                    sumToString[n] = []
                sumToString[n].append([i, j])

        # 判断
        results = {}
        for i in range(len(nums)):
            n = -nums[i]
            if sumToString.__contains__(n):
                for l in sumToString[n]:
                    # 是否使用了重复的元素
                    if i not in l:
                        t = l.copy()
                        t.append(i)
                        t.sort()
                        t = [self.nums[i] for i in t]

                        results[self.listToString(t)] = t
        return list(results.values())

    def listToString(self, l: List[int]) -> str:
        return '#'.join([str(i) for i in l])

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,0,1,2,-1,-4]')
    print('Output :')
    print(str(Solution().threeSum([-1, 0, 1, 2, -1, -4])))
    print('Exception :')
    print('[[-1,-1,2],[-1,0,1]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = []')
    print('Output :')
    print(str(Solution().threeSum([])))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [0]')
    print('Output :')
    print(str(Solution().threeSum([0])))
    print('Exception :')
    print('[]')
    print()

    pass
# @lc main=end