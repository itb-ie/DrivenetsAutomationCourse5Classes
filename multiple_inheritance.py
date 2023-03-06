class A:
    def do_something(self):
        print("A's implementation of do_something()")
    def e_method(self):
        print("inside A")

class B:
    def do_something(self):
        print("B's implementation of do_something()")

class C(B):
    def e_method(self):
        print("inside C")

class D(B, A):
    pass

class E(D, C):
    pass

print(E.mro())
e = E()
e.do_something()
e.e_method()
