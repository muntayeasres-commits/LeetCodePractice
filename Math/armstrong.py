def is_armistrong(n):
    sum=0
    for i in int(n):
        sum+=i
    if sum**len(n)==int(n):
        return True
    else:
        return False
x=123
n=str(x)
print(is_armistrong(n))
