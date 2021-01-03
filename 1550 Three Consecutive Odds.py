'''
URL: https://leetcode.com/problems/three-consecutive-odds/

Difficulty: Easy

Description: Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000

'''


class Solution:
    def threeConsecutiveOdds(self, arr):
        '''
        count = 0

        for n in arr:
            if n%2:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False
        '''

        i = 0
        while i < len(arr)-2:
            if arr[i] % 2:
                if arr[i+1] % 2 and arr[i+2] % 2:
                    return True
            i += 1

        return False
