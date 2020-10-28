a=[0,0]
for x in range(1,100000):
    i=0;b=x
    while b!=1:b=((b%2 ==0)*(b/2))+((b%2>0)*(3*b+1));i+=1
    if a[0]<i:a=[i,x]    
print(a[0])
