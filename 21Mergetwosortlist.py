list1 = [1,2,4]
list2 = [1,3,4]
#output [1,1,2,3,4,4]
new_list = list1 + list2
print(new_list)
for i in range(len(new_list)):
    for u in range(0,len(new_list)-i-1):
        if new_list[u+1] < new_list[u]:
            new_list[u], new_list[u+1] = new_list[u+1], new_list[u]


print(new_list)