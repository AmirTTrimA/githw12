a=input().split(',')

def fanck_1(x):
    sum=0
    for i in x:
        sum+=int(i)
    return sum/len(x)
print(fanck_1(a))
     