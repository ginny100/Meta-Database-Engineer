class A:
    def c(self):
        return "Function inside A"

class B(A):
    def c(self):
        return "Function inside B"

class C(A,B):
    pass

class D(C):
    pass

d = D()
print(d.a)

'''
Output:
Error on line 9:
    class C(A,B):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B
'''