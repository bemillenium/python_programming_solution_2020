# Christmas tree
# Write a program that p​ rint​ the christmas tree. The height of the tree is defined by n
# Input number: 5
#      *
#     ***
#    *****
#   *******
#  *********

number = 10
for i in range(number):
  for space in range(number-i-1):
    print(" ",end="")
  for star in range(2*i+1):
    print("*",end="")
  print()