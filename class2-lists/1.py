my_list = [1,22,22,4224,3,1,23,3,45]
output = []

for i in my_list:
    count = 0
    for j in my_list:
        if(i == j):
            count = count + 1
    if (count == 1):
        # print(i)
        output.append(i)

print(output)