# Class definition of A
class A:
    # Constructor for A
    def __init__(self, c):
        print("---------Inside class A----------")
        self.c = c
    print("Print inside A.")

    # Definition of local method alpha()
    def alpha(self):
        c = self.c + 1
        return c

print(dir(A))
print("Instantiating A..")
# Instantiating object a over class A
a = A(1) # To be commented out
# Calling method alpha() over object of class A
print(a.alpha()) # To be commented out

# Class definition of B
class B:
    # Constructor for B
    def __init__(self, a):
        print("---------Inside class B----------")
        self.a = a

    # Calling method alpha() over object of class A
    print(a.alpha()) # To be commented out
    d = 5
    print(d)
    print(a) # To be commented out

print("Instantiating B..")
# Instantiating object a over class B *.
b = B(a) # To be commented out
# Additional print statements distributed through the code.
print(a) # To be commented out