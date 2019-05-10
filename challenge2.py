start = 1
nxt = 2
res = 0
for i in range(0,50):
    # print('start :', start)
    if start >= 4000000:
        break
    if start % 2 == 0:
        res += start
        # print('res :', res)
    nxt1 = start + nxt
    start = nxt
    nxt = nxt1
   
print(res)