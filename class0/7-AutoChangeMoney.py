# 7. Change money
# โปรแกรมทอนเงิน
# โดยสามารถทอน ธนบัตร 500 100 50 20 เหรียญ 10 5 2 1 โดยจะไล่ทอนจาก มูลค่ามากไปก่อน
# เช่น
# ทอนเงิน 643 บาท
# โปรแกรมจะทอน 500 บาท 1 ใบ 100 บาท 1 ใบ 20 บาท สองใบ 1 บาท 3 เหรียญ
# ตัวอย่างโปรแกรม
# Give me a number?
# 643
# Your charge is
# 500: 1
# 100: 1
# 50: 0
# 20: 2
# 10: 0
# 5: 0
# 2: 0
# 1: 3
money = input("Give me a number\n")
money = int(money)
ch500 = money//500
money = money%500
ch100 = money//100
money = money%100
ch50 = money//50
money = money%50
ch20 = money//20
money = money%20
ch10 = money//10
money = money%10
ch5 = money//5
money = money%5
ch2 = money//2
money = money%2
ch1 = money
print("500: ",ch500)
print("100: ",ch100)
print("50: ",ch50)
print("20: ",ch20)
print("10: ",ch10)
print("5: ",ch5)
print("2: ",ch2)
print("1: ",ch1)