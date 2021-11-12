

def func1():
    global a
    a= 10
    print (f"func1()에서 a값 {a}")
def func2():
    print (f"func2()에서 a값 {a}")

a=20
func1()
func2()
print(a)