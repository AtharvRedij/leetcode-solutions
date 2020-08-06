'''
URL: https://leetcode.com/problems/day-of-the-week/

Difficulty: Easy

Description: Day of the Week

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.

'''


class Solution:
    def isLeapYear(self, year):
        return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

    def daysUntilYear(self, year):
        count = 0
        for y in range(1970, year):
            if self.isLeapYear(y):
                count += 366
            else:
                count += 365

        return count

    def daysUntilMonth(self, month, year):
        daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        count = 0

        for i in range(month-1):
            if i == 1 and self.isLeapYear(year):
                count += 29
            else:
                count += daysInMonths[i]

        return count

    def dayOfTheWeek(self, day, month, year):
        dayNames = ["Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday", "Saturday"]

        totalDays = 0

        totalDays += self.daysUntilYear(year)

        totalDays += self.daysUntilMonth(month, year)

        totalDays += day

        return dayNames[(totalDays + 3) % 7]
