#####my try
#  arr = []
# if len(arr) < 3 :
#     return False 
# last_num = 0
# if arr[0] != arr[-1]:
#     return False 
# for i in arr:
#     if i > last_num :
#         pass
#     else :
#         for i in range(len(arr),0,-1):
#             if arr[i] < arr[i-1]:
#                 return True
#         return False 
#     last_num = i 

def udemy(arr):
    a = arr
    i = 1 
    while(i < len(a) and a[i] > a[i-1]):
        i+=1 

    if i == 1 or i == len(a):
        return False

    while i < len(a) and a[i] < a[i-1]:
        i+= 1
    return i==len(a)