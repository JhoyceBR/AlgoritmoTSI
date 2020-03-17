n = int(input())
for i in range(n):
    l = input().split()
    a = l[0]
    b = l[1]
    s = ""

    if(len(a)==len(b)):
        for i in range(len(a)):
            s += a[i] + b[i]    
    elif(len(a)>len(b)):
        for i in range(len(b)):
            s += a[i] + b[i]
        s += a[len(b):]

    elif(len(b)>len(a)):
        for i in range(len(a)):
            s += a[i] + b[i]
        s += b[len(a):]
    
    print(s)
