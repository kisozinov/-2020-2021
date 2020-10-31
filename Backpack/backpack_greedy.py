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
#w = [4,3,1.5,0.5] # веса предметов
#c = [20,18,7,7] # стоимости
#N = len(w) # кол-во предметов
#max_capacity = 7 # вместимость рюкзака
already_filled = 0
total_cost = 0

unit_cost = [[None,w[i]] for i in range(N)]
for i in range(N):
    unit_cost[i][0] = c[i] / w[i]

unit_cost.sort(reverse = True)

for i in range(N):
    for j in range(2):
        print(unit_cost[i][j], end = '\t')
    print('')
i = 0

while (already_filled < max_capacity):
    if unit_cost[i][1] + already_filled <= max_capacity:
        already_filled += unit_cost[i][1]
        total_cost += unit_cost[i][0] * unit_cost[i][1]
    else:
        total_cost += unit_cost[i][0] * (max_capacity - already_filled)
        already_filled += (max_capacity - already_filled)
    i += 1
print(total_cost)
