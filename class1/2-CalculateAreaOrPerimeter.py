#​ Calulate Area or Perimeter of a Circular #​ Expected Output
#​ Please Choose Mode:
#​ 1. Area
#​ 2. Perimeter
#​ 1
#​ Please input R
#​ Area of this circular is _

PI = 22/7
print("Please Choose Mode:")
print("1. Area")
print("2. Perimeter")
mode = input()
r = input("Please input R ")
if mode == "1":
  print("The Area of this circular is",PI*float(r)**2)
else:
  print("The Perimeter of this circular is",2*PI*float(r))
