data1=[('A',8),('B',10),('C',2),('D',5),('E',6),('F',50)]
A=sorted(data1, key=lambda x: x[1])
print(A)
from operator import itemgetter
data2 = [
    {'uid': 3, 'name': 'Tom'},
    {'uid': 1, 'name': 'Amy'},
    {'uid': 2, 'name': 'John'}
]
B = min(data2, key=itemgetter('uid'))
print(B)