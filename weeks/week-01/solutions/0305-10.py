import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 8)
print(heapq.heappop(h))
from collections import deque
q = deque([0,10,0])
q.pop()#右邊刪除
q.popleft()#左邊刪除
q.append(100)#右邊加入
q.appendleft(70)#左邊加入
print(q)
class User:
    def __init__(self, user_id):
        self.user_id = user_id
u = User(42)
uid = u.user_id
print(uid)
# 例外處理
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
print(is_int("123"))
print(is_int("abc"))