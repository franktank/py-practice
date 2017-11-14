"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        res = []
        thousands_counter = 0
        while num > 0:
            rem = num % 1000
            if rem == 0:
                num /= 1000
                thousands_counter += 1
                continue
            rem_to_eng = self.helper(rem)
            res.insert(0, THOUSANDS[thousands_counter])
            res.insert(0, rem_to_eng)
            thousands_counter += 1
            num /= 1000
        return ' '.join(res).strip()



    def helper(self, rem):
        NUMBERS = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        res = []
        if rem >= 100:
            hundred = rem // 100
            res.append('{} Hundred'.format(NUMBERS[hundred]))
            rem = rem % 100
        if rem >= 20:
            t = (rem // 10)*10
            res.append(NUMBERS[t])
            rem = rem % 10
        if rem < 20 and rem > 0:
            res.append(NUMBERS[rem])

        return ' '.join(res)
