'''
URL: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

Difficulty: Easy

Description: Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.

'''


class Solution:
    def countCharacters(self, words, chars):
        chars_counts = {}

        for ch in chars:
            if ch in chars_counts:
                chars_counts[ch] += 1
            else:
                chars_counts[ch] = 1

        count = 0

        for string in words:
            flag = 0

            for ch in string:
                if not (ch in chars_counts and string.count(ch) <= chars_counts[ch]):
                    flag = 1
                    break

            if flag == 0:
                count += len(string)

        return count
