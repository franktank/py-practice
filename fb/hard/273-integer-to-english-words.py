"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
# Use % 1000
# Take result from %1000 and translate to english word
# Concatenate "", thousand, million, or billion to result from above
# Repeat until input is 0
# Categories: less than 20, tens, thousands

class Solution(object):
    def to_word(self, num):
        LESS_THAN_20 = [
            "", "One", "Two",
            "Three", "Four", "Five",
            "Six", "Seven", "Eight",
            "Nine", "Ten", "Eleven",
            "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]

        TENS = [
            "", "Ten", "Twenty",
            "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty",
            "Ninety"
        ]
        if num == 0:
            return ""
        elif num < 20:
            return LESS_THAN_20[num] + " "
        elif num < 100:
            return TENS[num / 10] + " " + self.to_word(num % 10)
        else:
            return LESS_THAN_20[num / 100] + " Hundred " + self.to_word(num % 100)
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        THOUSANDS = [
            "", "Thousand ", "Million ", "Billion "
        ]
        if num == 0:
            return "Zero"
        word = ""
        thousands_counter = 0
        while num > 0:
            if num % 1000 != 0:
                word = self.to_word(num % 1000) + THOUSANDS[thousands_counter] + word
            num /= 1000
            thousands_counter += 1

        return word.strip()
