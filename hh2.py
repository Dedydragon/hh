def func(minn, maxx):
    spisok = []
    if minn%2==0:
        if minn == 2: spisok.append(2)
        for i in range(minn+1, maxx+1, 2):
            check = True
            for j in range(3, i, 2):
                if i % j == 0:
                    check = False
                    break
            if check:
                spisok.append(i)
    else:
        for i in range(minn, maxx+1, 2):
            check = True
            for j in range(3, i, 2):
                if i % j == 0:
                    check = False
                    break
            if check:
                spisok.append(i)
    return spisok
