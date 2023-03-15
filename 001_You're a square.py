# #Given an integral number, determine if it's a square number:
# def is_square(n):
#     i=1
#     if(n>0):
#         while(i*i<=n):
#             if(i*i==n):
#                 return True
#             i+=1
#         return False
#     elif(n==0):
#         return True
#     else:
#         return False
#
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

#test
print(is_square(0))
