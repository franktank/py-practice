"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
class Solution(object):
    LESS_THAN_20 = [
        "", "One", "Two",
        "Three", "Four", "Five",
        "Six", "Seven", "Eight",
        "Nine", "Ten", "Eleven",
        "Twelve", "Thirteen", "Fourteen",
    ]

    TENS = [
        "", "Ten", "Twenty"
        "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty",
        "Ninety"
    ]

    THOUSANDS = [
        "", "Thousand", "Million", "Billion"
    ]
    def to_word(self, num):


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"
        word = ""
        thousands_counter = 0
        while num > 0:
            word = to_word(num % 1000) + THOUSANDS[thousands_counter] + word
        # Use % 1000
        # Take result from %1000 and translate to english word
        # Concatenate "", thousand, million, or billion to result from above
        # Repeat until input is 0
        # Categories: less than 20, tens, thousands
