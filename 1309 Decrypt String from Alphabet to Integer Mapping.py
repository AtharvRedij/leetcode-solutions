'''
URL: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

Difficulty: Easy

Description: Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 

Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.

'''


class Solution:
    def freqAlphabets(self, s):
        result = ""
        i = len(s)-1

        # iterate from backwards
        while i >= 0:
            # if # is encountered get two nums before #
            if s[i] == "#":
                num = int(s[i-2:i])
                i -= 3
            # else get current single num
            else:
                num = int(s[i])
                i -= 1

            # add char at start
            result = chr(96+num) + result

        return result
