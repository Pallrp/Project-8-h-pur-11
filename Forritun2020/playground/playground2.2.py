num = int(input("Input an int: ")) # Do not change this line
the_sum = 0
for i in range(1,num+1):
    for s in range(0,i):
        the_sum += 1
    print(the_sum)