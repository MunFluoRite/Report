Iterator Report
=============

##### 작성자 : 문형석(FluoRite)

목차
-------------
### 1. Iterator 란?
### 2. Iterable 한 타입
### 3. Iterator 예제코드



Iterator 란?
-------------
이터레이터는 '반복자'라는 의미로, 이터러블(Iterable, 순회 가능한 자료구조)의 요소를 탐색하기 위한 포인터로, next()함수를 가지고 있는 객체다.



Iterable한 타입
-------------
list, dict, set, str, bytes, tuple, range


Iterator 예제코드
-------------
>>> a = {1, 2, 3}

>>> dir(a)

['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

>>> a_iter = a.__iter__()

>>> type(a_iter)
<type 'setiterator'>

>>> next(a_iter)
1

>>> next(a_iter)
2

>>> next(a_iter)
3

>>> next(a_iter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
