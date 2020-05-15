# 6 . Printing current and previous number sum in a given number.
#
# Give me a number?
# 4
# Current Number 4 Previous Number  3  Sum:  7

current_number = int(input("Give me a number?\n"))
previous = current_number - 1

print("Current Number ",current_number," Previous Number ",previous, "Sum ",previous+current_number)