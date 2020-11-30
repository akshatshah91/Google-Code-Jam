testCases = int(input())
for x in range(testCases):
    houses = 0
    line = input().split()
    n = int(line[0])
    b = int(line[1])
    a = input().split()
    for y in range(n):
        a[y] = int(a[y])
    a.sort()
    for y in range(n):
        b -= a[y]
        if b < 0:
            break;
        houses += 1
    print("Case #", x+1, ": ", houses, sep='')