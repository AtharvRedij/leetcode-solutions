'''
URL: https://leetcode.com/problems/count-largest-group/

Difficulty: Easy

Description: Count Largest Group

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5
 

Constraints:

1 <= n <= 10^4

'''


class Solution:
    def sumOfDigits(self, n):
        sum = 0

        while n > 0:
            sum += n % 10
            n = n // 10

        return sum

    def countLargestGroup(self, n):
        counts = {}

        for i in range(1, n+1):
            # sum of the digits of n
            sum = self.sumOfDigits(i)

            if sum in counts:
                counts[sum].append(i)

            else:
                # if sum is not in dict
                # store in format
                # key: sum
                # value: [ All the elements that sum to that size ]
                counts[sum] = [i]

        largestGroupSize = -float('inf')
        largestGroupCount = 0

        for group in counts.values():
            size = len(group)

            if size > largestGroupSize:
                largestGroupSize = size
                largestGroupCount = 1

            elif size == largestGroupSize:
                largestGroupCount += 1

        return largestGroupCount
