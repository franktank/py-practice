class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur_string = ""
        stack = list(s)
        while stack:
            counter = 0
            if stack[len(stack)-1] == "]":
                counter += 1
                stack.pop()
                i = len(stack)-1
                j = len(stack)
                while stack and counter > 0:
                    if stack[i] == "]":
                        counter += 1
                    elif stack[i] == "[":
                        counter -= 1
                    stack.pop()
                    i -= 1
                ret_str = self.decodeString(s[i+2:j])
                if stack[len(stack)-1].isdigit():
                    d = ""
                    while stack and stack[len(stack)-1].isdigit():
                        d = stack.pop() + d
                    ret_str = int(d)*ret_str
                cur_string = ret_str + cur_string
            else:
                cur_string = stack.pop() + cur_string
        return cur_string
