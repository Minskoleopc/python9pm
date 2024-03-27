class A(object):
    def add(self):
        print("A class method is called") # 3
        super().add()

class B(object):
    def add(self):
       print("B class method is called") # 5
       super().add()

class C(object):
    def add(self):
        print("C class method is called") # 6


class X(A,B):
    def add(self):
        print("X class method") #2
        super().add()

class Y(B,C):
    def add(self):
        print("Y class method") # 4
        super().add()

class P(X,Y,C):
    def add(self):
        print("P class method") # 1
        super().add()

p = P()
p.add()




