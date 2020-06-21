'''
URL: https://leetcode.com/problems/increasing-decreasing-string/

Difficulty: Easy

Description: Increasing Decreasing String

Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
Example 3:

Input: s = "leetcode"
Output: "cdelotee"
Example 4:

Input: s = "ggggggg"
Output: "ggggggg"
Example 5:

Input: s = "spo"
Output: "ops"
 

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.

'''

# this solution works but isn't very good, try to find a better one


class Solution:
    def nextGreater(self, s, char):
        greater = []

        for i, ch in enumerate(s):
            if ch > char:
                greater.append((i, ch))

        if len(greater) == 0:
            return (-1, "")
        else:
            return sorted(greater, key=lambda x: x[1])[0]

    def nextSmaller(self, s, char):
        smaller = []

        for i, ch in enumerate(s):
            if ch < char:
                smaller.append((i, ch))

        if len(smaller) == 0:
            return (-1, "")
        else:
            return sorted(smaller, key=lambda x: x[1])[-1]

    def sortString(self, s):
        if len(s) <= 0:
            return ""

        index = s.index(min(s))
        last_appended_char = s[index]
        s = s[:index] + s[index+1:]
        result = last_appended_char

        while len(s) > 0:
            i, ch = self.nextGreater(s, last_appended_char)
            if i == -1:
                break
            result += ch
            s = s[:i] + s[i+1:]
            last_appended_char = ch

        if len(s) > 0:
            index = s.index(max(s))
            last_appended_char = s[index]
            s = s[:index] + s[index+1:]
            result += last_appended_char

        while len(s) > 0:
            i, ch = self.nextSmaller(s, last_appended_char)
            if i == -1:
                break
            result += ch
            s = s[:i] + s[i+1:]
            last_appended_char = ch

        return result + self.sortString(s)
