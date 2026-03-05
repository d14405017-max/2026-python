data=[1,-2,3,-4]
a=[x for x in data if x > 0]
print(a)
b=[('a',1),('b',2)]
c={k:v for k,v in b}
print(c)
d=sum(n*n for n in data)
print(d)