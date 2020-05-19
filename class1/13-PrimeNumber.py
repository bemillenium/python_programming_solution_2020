# ​ Write a program that show the prime number between 2 given number(both included) #​ Expected output
# ​ Enter a number
# ​ 5
# ​ 5 is prime number
# ​ 6
# ​ 6 is not prime number

number = 9
if (number==1 or number == 2):
  print(number, "is prime number")
else:
  divide_end = number // 2
  start_divide_number = 3
  while(start_divide_number <= divide_end):
    if (number%start_divide_number == 0):
      break
    start_divide_number = start_divide_number+1
  if start_divide_number>divide_end:
    print(number, "is prime number")
  else:
    print(number, "is not prime number")