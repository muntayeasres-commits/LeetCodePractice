def is_armistrong(n):
    sum=0
    for i in n:
        sum+=int(i)**len(n)
    if sum==int(n):
        return True
    else:
        return False
x=123
n=str(x)
print(is_armistrong(n))
