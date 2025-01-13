# people = [3,2,2,1]
# limit = 3
# new_boat = 0
# boat = 0
# x = len(people)-1

# for i in range(x):
#     for j in range(0,x):
#         if people[i] + people[j] <= limit:
#             print(f'i{people[i]} j{people[j]}')
#             boat += 1
#             # people.remove(people[i])
#     if boat < new_boat :
#         boat += 1 
#     new_boat = boat 
# print(boat)


#####note no one weight more than boat and no one weight == 0

people.sort()
last_person = len(people) - 1 
first_person = 0
boats = 0 

def udemy():
    while last_person >= first_person :
        if people[last_person] + people[first_person] <= limit :
            first_person += 1 
            last_person -= 1
        else :
            last_person -= 1
        boats += 1
    return boats
