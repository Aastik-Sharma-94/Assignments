class A:
    def _init_(self):
        print('a')
    def m1(self):
        print('m1')
class b(A):
    a=4
    b=5
    def m2(self):
        print(self.a,self.b)
ob=b()
ob.m1()
ob.m2()