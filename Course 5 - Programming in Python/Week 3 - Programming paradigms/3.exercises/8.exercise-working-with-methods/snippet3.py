class A:
    pass

class B(A):
    pass

class C(B):
    pass


c = C()
print(c.a())

'''
Output:
Error on line 12:
    print(c.a())
AttributeError: 'C' object has no attribute 'a'
'''