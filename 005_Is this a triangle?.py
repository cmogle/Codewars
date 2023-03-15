def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
#
# a = int(input("Enter the length of side a: "))
# b = int(input("Enter the length of side b: "))
# c = int(input("Enter the length of side c: "))
#
# result = is_triangle(a, b, c)
#
# if result:
#     print("A triangle can be built with the given side lengths.")
# else:
#     print("A triangle cannot be built with the given side lengths.")
