#​ Write a Python program to construct the following pattern, using a nested loop number. Go to the editor
#​ Expected Output:
#​ Input number:
#​ 9
#​ 1
#​ 22
#​ 333
#​ 4444
#​ 55555
#​ 666666
#​ 7777777 #​ 88888888 #​ 999999999

number = input("Input number: ")
for i in range(int(number)):
  print(int(i+1)*str(int(i+1)))

for i in range(int(number)):
  for j in range(i+1):
    print(i+1,end="")
  print()