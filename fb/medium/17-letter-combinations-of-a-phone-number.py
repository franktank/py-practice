"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        digit_mapping = dict()
        digit_mapping['2'] = ['a','b','c']
        digit_mapping['3'] = ['d','e','f']
        digit_mapping['4'] = ['g','h','i']
        digit_mapping['5'] = ['j','k','l']
        digit_mapping['6'] = ['m','n','o']
        digit_mapping['7'] = ['p','q','r','s']
        digit_mapping['8'] = ['t','u','v']
        digit_mapping['9'] = ['w','x','y','z']

        combinations = list()
        for letter in digit_mapping[digits[0]]:
            combinations.append(letter)

        for idx, digit in enumerate(digits):
            if idx == 0:
                continue
            new_combinations = list()
            for letter in digit_mapping[digit]:
                for combination in combinations:
                    new_combinations.append(combination + letter)
            combinations = list(new_combinations)
        return combinations
