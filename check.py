def check_plate(s):
    x=s[0:2]+s[4:]
    x1=s[2:4]
    for i in x:
        if i<'0' or i>'9':
            return 0
    for i in x1:
        if i<'A' or i>'Z':
            return 0
    return 1
# s="58FA8889"
# print(check(s))