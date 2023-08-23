N = int(input())
z = []
for i in range(0,N):
    x = input()
    y = []
    y = x.split(" ")
    if y[0] in "insert":
        z.insert(int(y[1]),int(y[2]))
    elif y[0] in "print":
        print(z)
    elif y[0] in "remove":
         z.remove(int(y[1]))
    elif y[0] in "append":
        z.append(int(y[1]))
    elif y[0] in "sort":
        z.sort()
    elif y[0] in "pop":
        z.pop(-1)
    elif y[0] in "reverse":
        z = z[::-1]