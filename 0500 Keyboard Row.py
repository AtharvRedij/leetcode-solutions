'''
URL: https://leetcode.com/problems/keyboard-row/

Difficulty: Easy

Description: Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 



 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''


class Solution:
    def findWords(self, words):
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        output = []

        for word in words:
            word_set = set(word.lower())

            for row in rows:
                if word_set.issubset(row):
                    output.append(word)
                    break

        return output
