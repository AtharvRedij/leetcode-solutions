'''
URL: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Difficulty: Easy

Description: Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

'''


class Solution:
    def replaceElements(self, arr):
        largest = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            n = arr[i]

            arr[i] = largest

            if n > largest:
                largest = n

        return arr

        '''
        Other solution
        
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
            
        arr[-1] = -1
        return arr        
        
        '''
