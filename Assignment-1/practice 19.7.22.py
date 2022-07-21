class A ():
    a=89
    b=70
    def __init__(self, a, b):
       self .a=a
    def f1(self,a,b):
        print (a+b)
        print(self.a+self.b)
ob=A(12,34)
ob.f1 (12,45)       