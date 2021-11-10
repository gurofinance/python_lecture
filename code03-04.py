sel = int(input("진수 타입을 넣으시오(16/10/8/2)"))
num = input('값 입력:')

if sel == 16:
    num10 = int(num, 16)
    print(num10)
    print(hex(num10))
    print(bin(num10))

if sel == 2:
    num2 = int(num, 2)
    print(num2)
    print(bin(num2))
    print(hex(num2))
