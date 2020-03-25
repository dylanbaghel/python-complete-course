"""
Diamond Problem:
    A
  /   \
  B   C
   \ /
    D
# Order -> D, B, C, A, Object
"""
class A:
    def msg(self):
        print('Defined In Class: A')

class B(A):
    def msg(self):
        print('Defined In Class: B')

class C(A):
    def msg(self):
        print('Defined In Class: C')

class D(B, C):
    def msg(self):
        print('Defined In Class: D')


d = D()
d.msg()
print(D.__mro__)
print(D.mro())