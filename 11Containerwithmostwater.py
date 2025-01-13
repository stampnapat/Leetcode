# count = 0
# max_area = 0
# for n in height :
#     area = count * n
#     max_area = max(area,max_area)
#     count += 1


#my try but time limit in leetcode exceeded
height = [1,8,6,2,5,4,8,3,7]
x = len(height)
max_area = 0
for i in range(x) :
    for u in range(1,x) :
        # print(f'i{i} and u{u}')
        width = u-i
        area =  min(height[i],height[u]) * width
        max_area = max(area,max_area)


print(max_area)








####udemy 

front_side = 0
back_side = len(height) -1 
max_area = 0
while front_side < back_side :
    length = min(height[front_side],height[back_side])
    width = back_side - front_side 
    area = length * width
    max_area = max(area,max_area)
    if height[front_side] < height[back_side] :
        print(f'front {front_side}')
        front_side += 1

    else : 
        print(f'back {back_side}')
        back_side -= 1

    print(f'area {max_area}')

    # return max_area

# print(max_area)