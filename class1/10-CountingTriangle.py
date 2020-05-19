#​ Write a Python program to construct the following pattern, using a nested loop number. Go to the editor
#​ Expected Output:
#​ Input number:
#​ 9
#​ 1
#​ 12
#​ 123
#​ 1234
#​ 12345
#​ 123456
#​ 1234567 
#​ 123456789

number = 9
for i in range(number+1):
  for j in range(i):
    print(j+1,end="")
  print()

