def arm(x,y):
    lst=[]
    for i in range (x,y):
        total =0
        for j in str(i):
            total +=(int(j)**3)
        if total == i:
            lst.append(i)
    return lst
print(arm(1,1000))


def pal(x,y):
    l=[]
    for i in range(x,y):
        if str(i) ==str(i)[::-1]:
            l.append(i)
    return l
print(pal(2,345))