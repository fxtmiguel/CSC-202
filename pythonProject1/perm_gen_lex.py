def perm_gen_lex(list1):
    perm_list = []  # makes perm list
    if len(list1) == 1:
        return list1
    for char in list1:  # goes through list
        for x in perm_gen_lex(list1.replace(char, '', 1)):  # replaces char with space
            perm_list.append(char + x)
    return perm_list


