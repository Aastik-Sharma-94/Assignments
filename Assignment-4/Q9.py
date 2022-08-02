class Vehicle:
    def __del__(self):
        print("Vehicle object destroyed")
        print(8/0)
v = Vehicle()
del v