'''
URL: https://leetcode.com/problems/two-sum/

Difficulty: Easy

Description: Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            n = nums[i]
            comp = target-n

            if n == comp:
                temp = nums.copy()
                temp.remove(n)

                if comp not in temp:
                    continue

            if comp in nums:
                if n == comp:
                    temp = nums.copy()
                    temp.remove(n)
                    j = temp.index(comp) + 1
                    return [i, j]
                else:
                    j = nums.index(comp)
                    return [i, j]
