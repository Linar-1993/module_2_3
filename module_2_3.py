my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
z = 0
while z < len(my_list):
    if my_list[z] == 0:
        z += 1
        continue
    if my_list[z] <= -1:
        break
    print(my_list[z])
    z += 1





