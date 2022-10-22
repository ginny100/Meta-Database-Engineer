# Exercise: Working with Methods

1. Guess the output for the following block of code and try running the code once you have a solution in mind:

```python
class A:
    def b(self):
        return "Function inside A"

class B:
    pass

class C:
    def b(self):
        return "Function inside C"

class D(B, C, A):
    pass

class D(C):
    pass

d = D()
print(d.b())
```

2. Guess the output for the following block of code and try running the code once you have a solution in mind:

```python
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
```

3. Guess the output for the following block of code and try running the code once you have a solution in mind:
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass


c = C()
print(c.a())
```