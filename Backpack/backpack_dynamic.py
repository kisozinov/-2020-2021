
f = open("backpack_data.txt",'r')
N = int(f.readline())
max_capacity = int(f.readline())
w = f.readline().replace("\n", "").split(' ')
c = f.readline().replace("\n", "").split(' ')
f.close()
for i in range(len(w)):
    w[i] = int(w[i])
for i in range(len(c)):
    c[i] = int(c[i])

table = [[0] * (max_capacity+1) for i in range (N+1)]

for i in range(N+1):
    print('\n')
    for j in range(max_capacity+1):
        print(table[i][j], end = '\t')
print('\n')

for i in range(1,N+1):
    for j in range(max_capacity+1):
        if w[i-1] > j:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(c[i-1]+table[i-1][j-w[i-1]],table[i-1][j])

for i in range(1,N+1):
    print('\n')
    for j in range(1,max_capacity+1):
        print(table[i][j], end = '\t')