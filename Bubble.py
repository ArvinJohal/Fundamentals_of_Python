list = [5,3,2,8]

swapped = False

swap = 0

count = 1

len_list = len(list)

while swapped == False:

    while count < len_list:

        j = count - 1

        if list[count] < list[j]:

            temp = list[count]

            list[count] = list[j]

            list[j] = temp

            swap += 1

        count += 1

    if swap == 0:

        swapped = True

    else:

        swap = 0

        count = 1

print(list)