'''
URL: https://leetcode.com/problems/string-matching-in-an-array/

Difficulty: Easy

Description: String Matching in an Array

Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.

'''


class Solution:
    def stringMatching(self, words):
        substrings = []

        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if word1 in word2 and i != j:
                    substrings.append(word1)

        return list(set(substrings))
