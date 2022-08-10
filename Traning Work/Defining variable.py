a=10
def f():
    print ('inside f',a)
    def g():
      b=20
    print(b)
    print('inside g',a)