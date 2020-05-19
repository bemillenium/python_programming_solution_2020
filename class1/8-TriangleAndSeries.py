# Triangle and series
# Write a python program that print a triangle.
#The* ​of​ eachfloor ​of​ triangleisanumber ​of​ *i​ n​ theterm ​of​ (1​ ,​ 3​ ,​ 5​ ,​ 7​ ,​ 9​ ,​ ...)

number = 8
for i in range(number):
  for j in range(2*i+1):
    print("*",end="")
  print()