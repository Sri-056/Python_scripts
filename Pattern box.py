N = int(input())
s = (N * 2) - 1
s1=s-1
q=N
t=0
m = [[0 for i in range(s)] for j in range(s)]
for i in range(N-1):
    for j in range(t,s1+1):
        m[t][j]=q
        m[j][t]=q
        m[j][s1]=q
        m[s1][j]=q
    t=t+1
    q=q-1
    s1=s1-1
for i in m:
    print(i,q)