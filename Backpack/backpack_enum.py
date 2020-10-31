#from typing import list
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

#w = [3,2,3,4]
#c = [1,2,2,4]
#N = len(w)
#max_capacity = 6

def rec(i:int, ww:int):
    if (i < 0):
        return 0
    t = 0
    if w[i] + ww <= max_capacity:
        t = rec(i-1, w[i] + ww) + c[i]

    return max(t,rec(i-1,ww))
print(rec(N-1,0))
