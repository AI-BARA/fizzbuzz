i = 0
while True:
    i += 1
    if i % 3 ==0:
        p = 'サン'
    elif '3' in str(i):
        p = 'サン！！'
    else:
        p = i
    print(p)
    if i == 100:
        break