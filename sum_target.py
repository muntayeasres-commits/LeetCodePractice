x=[2,7,11,15]
target=9
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==target:
            print(f'[{i},{j}]')