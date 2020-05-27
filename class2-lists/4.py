A_list = [1,22,22,4224,3,1,23,3,45, 68, 20, 24]
B_list = [1,22,22,4224,3,1,23,3,45, 34, 65]

output=[]
for i in A_list:
    if i not in B_list:
        output.append(i)
print(output)
