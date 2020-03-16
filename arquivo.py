n = int(input())
for i in range(n):
    l = input().split()
    a = l[0]
    b = l[1]
    s = ""

    menor = min(len(a), len(b))
    maior = max(len(a), len(b))
    for i in range(menor):
        s += a[i] + b[i]
    if(len(a)==len(b)):
        pass
    
    elif(len(a)>len(b)):
        diferenca = len(a)-len(b)
        s += a[diferenca:]
    elif(len(b)>len(a)):
        diferenca = len(b)-len(a)
        s += b[diferenca:]
    
    
    print(s)
