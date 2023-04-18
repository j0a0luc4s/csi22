class A:
    def whatami(self):
        print("I'm a class")
    def hi(self):
        print("I'm A")

class B(A):
    def hi(self):
        print("I'm B")

class C(A):
    def hi(self):
        print("I'm C")

class D(B, C):
    def whatami(self):
        print("I'm a subderived class")

a = A()
b = B()
c = C()
d = D()

objects = [a, b, c, d]

for object in objects:
    object.hi()
    object.whatami()
