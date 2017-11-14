class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split("\n")
        res = 0
        root = 0
        cur_string = [paths[0]]
        prev_t_count = 0
        for j in range(1,len(paths)):
            cur_t_count = paths[j].count("\t")
            if cur_t_count < prev_t_count:
                paths[j] = re.sub('\t', '', paths[j])
                cur_string = [paths[0], '/', paths[j]] # pop until i?
                prev_t_count = cur_t_count
            elif cur_t_count == prev_t_count: # same level
                paths[j] = re.sub('\t', '', paths[j])
                cur_string.pop()
                cur_string.append(paths[j])
            else:
                paths[j] = re.sub('\t', '', paths[j])
                cur_string.append('/')
                cur_string.append(paths[j])
                prev_t_count = cur_t_count
            if "." in paths[j]:
                print(cur_string)
                print("".join(cur_string))
                res = max(res, len("".join(cur_string)))
        if "." in "".join(cur_string):
            print("".join(cur_string))
            res = max(res, len("".join(cur_string)))
        return res

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split("\n")
        res = 0
        root = 0
        cur_string = [paths[0]]
        prev_t_count = 0
        for j in range(1,len(paths)):
            cur_t_count = paths[j].count("\t")
            if cur_t_count <= prev_t_count:
                while cur_t_count <= prev_t_count:
                    cur_string.pop()
                    if cur_string[len(cur_string)-1] == "/":
                        cur_string.pop()
                        continue
                    prev_t_count = cur_string[len(cur_string)-1].count("\t")
                paths.append(paths[j])
            elif cur_t_count == prev_t_count: # same level
                paths[j] = re.sub('\t', '', paths[j])
                cur_string.pop()
                cur_string.append(paths[j])
            else:
                paths[j] = re.sub('\t', '', paths[j])
                cur_string.append('/')
                cur_string.append(paths[j])
                prev_t_count = cur_t_count
            if "." in paths[j]:
                print(cur_string)
                print("".join(cur_string))
                res = max(res, len("".join(cur_string)))
        if "." in "".join(cur_string):
            print("".join(cur_string))
            res = max(res, len("".join(cur_string)))
        return res



class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split("\n")
        res = 0
        root = 0
        cur_string = [paths[0]]
        prev_t_count = 0
        for j in range(1,len(paths)):
            cur_t_count = paths[j].count("\t")
            if cur_t_count <= prev_t_count:
                while cur_t_count <= prev_t_count and cur_string:
                    if cur_string:
                        if cur_string[len(cur_string)-1] == "/":
                            cur_string.pop()
                            continue
                        else:
                            prev_t_count = cur_string[len(cur_string)-1].count("\t")
                            if prev_t_count < cur_t_count:
                                break
                            else:
                                cur_string.pop()
                if cur_t_count > 0:
                    cur_string.append('/')
                cur_string.append(paths[j])
            else:
                cur_string.append('/')
                cur_string.append(paths[j])
                prev_t_count = cur_t_count
            if "." in paths[j]:
                s = "".join(cur_string).replace('\t','')
                res = max(res, len(s))
        if "." in "".join(cur_string):
            s = "".join(cur_string).replace('\t','')
            res = max(res, len(s))
        print(cur_string)
        s = "".join(cur_string).replace('\t','')
        print(s)
        return res
