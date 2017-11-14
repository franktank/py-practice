# Complete the function below.

def  runLengthEncode(input):
    cur_char = input[0]
    cur_count = 0
    res = []
    for i in range(len(input)):
        if not input[i] == cur_char:
            res.append(str(cur_count))
            res.append(cur_char)
            cur_char = input[i]
            cur_count = 1
        else:
            cur_count += 1
    res.append(str(cur_count))
    res.append(cur_char)
    return "".join(res)
