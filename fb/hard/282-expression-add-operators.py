"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
class Solution(object):
    OPERATORS = ['', '+', '-', '*']

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # Create all possible expressions and evaluate at each level
        # At each level, save all mappings of expression to value
        # After last level, find which key value mappings have value of target
        # Iterate num, and try all operators with next number
        # Use eval at end
        OPERATORS = ['', '+', '-', '*']
        expressions = set()
        expressions.add(num[0])
        for idx, element in enumerate(num):
            if idx == 0:
                continue
            new_expressions = set()
            for expression in expressions:
                for op in OPERATORS:
                    if op == '' and expression[len(expression) - 1] == '0':
                        continue
                    new_expressions.add(expression + op + element)
            expressions = set(new_expressions)

        valid_expressions = list()
        for e in expressions:
            if eval(e) == target:
                valid_expressions.append(e)

        return valid_expressions
