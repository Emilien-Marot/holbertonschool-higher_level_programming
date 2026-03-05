#!/usr/bin/python3
def cursor_detector(string, idx):
    if idx < 0 or idx >= len(string):
        return
    var_idx = 0
    new_idx = None
    hyphen = False
    if string[idx] == "-":
        if idx+1 < len(string) and idx-1 >= 0:
            if string[idx+1].isalnum() and string[idx-1].isalnum():
                hyphen = True
                new_idx = idx
    while not hyphen and idx+var_idx < len(string) and idx-var_idx >= 0:
        if idx+var_idx < len(string):
            if string[idx+var_idx].isalnum():
                new_idx = idx+var_idx
                break
        if idx-var_idx >= 0:
            if string[idx-var_idx].isalnum():
                new_idx = idx-var_idx
                break
        var_idx += 1
    if new_idx is None:
        return
    var_idx = 0
    idx_min = 0
    while new_idx-var_idx >= 0:
        if string[new_idx-var_idx] != "-" and not string[new_idx-var_idx].isalnum():
            idx_min = 1+new_idx-var_idx
            break
        if string[new_idx-var_idx] == "-":
            if new_idx-var_idx == 0:
                idx_min = 1+new_idx-var_idx
                break
            if not string[new_idx-(var_idx+1)].isalnum():
                idx_min = 1+new_idx-var_idx
                break
        var_idx += 1
    var_idx = 0
    idx_max = len(string)-1
    while new_idx+var_idx < len(string):
        if string[new_idx+var_idx] != "-" and not string[new_idx+var_idx].isalnum():
            idx_max = new_idx+var_idx-1
            break
        if string[new_idx+var_idx] == "-":
            if new_idx+var_idx == len(string)-1:
                idx_max = new_idx+var_idx-1
                break
            if not string[new_idx+var_idx+1].isalnum():
                idx_max = new_idx+var_idx-1
                break
        var_idx += 1
    print(string[idx_min:idx_max+1])

cursor_detector("", 15)