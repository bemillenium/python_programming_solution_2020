 # W​ rite​ a p​ rogram​ that calculate the average ​value​ of n ​value​, ​if​ you enter ​"s",​ # the p​ rogram​ will be ​stop


sum = 0
count = 0
while True:
  num = input("> ")
  if (num == 's' or num == 'S'):
    break
  sum = sum + float(num)
  count = count + 1
print("The average value of ",count,"number(s) is ",sum/count)
