f = open("E:/toanco.txt", "r")
l = f.readline()

while l:
    print(l, end="")
    l = f.readline()

f.close()