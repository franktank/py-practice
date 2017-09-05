"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
class Solution(object):
    def convert_to_number(self, bin):
        int_bin = int(bin)
        number = 0
        two_power = 0
        while int_bin > 0:
            if int_bin % 10 == 1:
                number += 2**two_power
            two_power += 1
            int_bin /= 10
        return number

    def convert_to_binary(self, num):
        bin_str = ''
        if num == 0:
            return '0'
        while num > 0:
            if num % 2 == 1:
                bin_str = '1' + bin_str
            else:
                bin_str = '0' + bin_str
            num /= 2
        return bin_str
        
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        add_sum = self.convert_to_number(a) + self.convert_to_number(b)
        return self.convert_to_binary(add_sum)
