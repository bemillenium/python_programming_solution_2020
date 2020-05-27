#2
My_list = [1,22,22,4224,3,1,23,3,45]

My_list_filter  = []
for i in My_list:
    if i not in My_list_filter:
        My_list_filter.append(i)

print(My_list_filter)
My_list_filter.sort()
print(My_list_filter)
print(My_list_filter[1])

#3
My_list = [1,22,22,4224,3,1,23,3,45]

My_list_filter  = []
for i in My_list:
    if i not in My_list_filter:
        My_list_filter.append(i)

print(My_list_filter)
My_list_filter.sort()
print(My_list_filter)
print(My_list_filter[len(My_list_filter)-2])

