# # a = 10 
# # b = 20
# def print_var():
#     a = 30
#     print(a)


# def print_var_1():
#     print(a)
# # c =print_var() 
# print_var_1()

def add_1(n):
      return n + 1

target = [1, 2, 3, 4, 5]

result = list(map(add_1, target))

print(result) 