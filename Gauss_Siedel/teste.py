import pandas as pd

ll : list[list[int]] = [ [ (4*i)+j for j in range(1,5)] for i in range(3)]

r = pd.DataFrame(data=ll, columns=[ '' for i in range(4)], index=[ '' for i in range(3)])

print(r)

for i in range(len(ll[0])):
    for j in range(len(ll)):
         t = ll[j][i]
         print(t)
    print('='*4)