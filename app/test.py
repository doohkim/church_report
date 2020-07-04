case = int(input())
bb = [input().split(' ') for _ in range(case)]
for i in range(len(bb)):
    for j in range(i+1, len(bb)):
        if int(aa[i][0]) < int(bb[j][0]):
            temp = bb[i]
            bb[i] = bb[j]
            bb[j] = temp
        if int(aa[i][0]) == int(bb[j][0]):
            temp = bb[i]
            bb[i] = bb[j]
            bb[j] = temp
bb.reverse()
for age, name in bb:
    print(age, name)
