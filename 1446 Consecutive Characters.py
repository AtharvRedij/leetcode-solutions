'''
URL: https://leetcode.com/problems/consecutive-characters/

Difficulty: Easy

Description: Consecutive Characters

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.

'''


class Solution:
    def maxPower(self, s):
        max_power = 1
        power = 1
        prev = s[0]

        for current in s[1:]:
            if prev == current:
                power += 1
            else:
                max_power = max(max_power, power)
                power = 1

            prev = current

        # edge case: string with only 2 same chars
        max_power = max(max_power, power)

        return max_power
