#​ Write a Python program to create the multiplication table (from 1 to 10) of a number. Go to the editor
#​ Expected Output: #
#​ Input a number: 6
#​ 6 x 1 = 6
#​ 6x2=12
#​ 6x3=18
#​ 6x4=24
#​ 6x5=30
#​ 6x6=36
#​ 6x7=42
#​ 6x8=48
#​ 6x9=54
#​ 6x10=60

number = 6
for i in range(10):
  print(number ,"x ", i+1,"= ", number*(i+1))