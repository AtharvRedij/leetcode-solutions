'''
URL: https://leetcode.com/problems/maximum-number-of-balloons/

Difficulty: Easy

Description: Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.

'''


class Solution:
    def maxNumberOfBalloons(self, text):
        counts = {}
        chars = set(['b', 'a', 'l', 'o', 'n'])

        for ch in text:
            if ch in chars:
                if ch in counts:
                    counts[ch] += 1
                else:
                    counts[ch] = 1

        if set(counts.keys()) != chars or counts['l'] < 2 or counts['o'] < 2:
            return 0
        else:
            counts['l'] = counts['l'] // 2
            counts['o'] = counts['o'] // 2

        min_count = float('inf')

        for _, count in counts.items():
            min_count = min(min_count, count)

        return min_count

        '''
        SLOWER METHOD
        
        text = list(text)
        chars = list('balloon')
        count = 0
        i = 0
        
        
        while True:
            if chars[i] in text:
                text.remove(chars[i])
            else:
                break
            
            i = (i+1) % 7
            
            if i == 0:
                count += 1
            
        return count
        
        
        '''
