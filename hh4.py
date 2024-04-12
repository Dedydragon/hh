def sortStr(strings):
    strings.sort(key=len)
    print(strings)
    strings.sort(key=len, reverse=True)
    print(strings)
