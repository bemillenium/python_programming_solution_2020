# Write a program that asks the user how many Fibonnaci numbers t​ o​ ​generate​ ​and then​ generates them.
# Take this opportunity ​to​ think about how you can u​ se​ functions.
# Make sure ​to​ ask the user ​to​ enter the number ​of​ numbers ​in​ the s​ equence​ ​to generate.​
# (Hint: The Fibonnaci seqence ​is​ a s​ equence​ ​of​ numbers where the n​ ext​ number ​in the s​ equence​ ​is​ the
# sum o​ f​ the previous two numbers i​ n​ the ​sequence​. The s​ equence​ looks like this: ​1​, 1,​ 2​ ,​ 3​ ,​ ​5​, ​8​, 1​ 3​, ...)

number = 9
current = None
last_number = None
last_last_number = None

for i in range(number):
  if i == 0:
    last_number = 0
    print(last_number)
    
  elif i == 1:
    last_number = 1
    last_last_number = 0
    print(last_number)
    
  else:
    current = last_last_number + last_number
    print (current)
    last_last_number = last_number
    last_number = current