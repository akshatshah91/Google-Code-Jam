testCases = int(input())
for x in range(testCases):
    n,k,p = map(int, input().split())
    plates = []
    allocation = []
    platesLeft = k*p
    for y in range(n):
        plateStack = input().split()
        plates.append(plateStack.reverse())
    while platesLeft > n:
        min = int(plates[0][0])
        loc = 0
        for y in range(1, len(plates)):
            if(int(plates[y][0]) < min):
                min = int(plates[y][0])
                loc = y
        del(plates[y][0])
        if len(plates[y]) == 0:
            del(plates[y])
    maxBeauty = 0
    for y in range(len(plates)):
        for z in range(len(plates[y])):
            maxBeauty += int(plates[y][z])
    print("Case #", x+1, ": ", maxBeauty, sep='')