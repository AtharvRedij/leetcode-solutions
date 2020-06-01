'''
URL: https://leetcode.com/problems/reverse-integer/

Difficulty: Easy

Description: Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


class Solution:
    def reverse(self, x):

        UPPER_LIMIT = (2**31)-1
        LOWER_LIMIT = -(2**31)

        isNegative = x < 0
        if isNegative:
            x = x*-1

        num = int(str(x)[::-1])

        if num > UPPER_LIMIT or num < LOWER_LIMIT:
            return 0

        if isNegative:
            return num*-1
        else:
            return num
