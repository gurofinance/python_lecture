
def func1() :
    result = 100
    return result

def func2(x) :
    print(f"func2()의 반환값은 ==> {x}")

sum = 0

sum = func1()
print(f"func1()의 반환값은 ==> {sum}")
func2(sum)