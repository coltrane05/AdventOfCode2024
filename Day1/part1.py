
list1 = []
list2 = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        line_split = line.split()
        list1.append(int(line_split[0]))
        list2.append(int(line_split[1]))
        line = file.readline()


total_distance = 0
while list1:
    min1 = min(list1)
    min2 = min(list2)
    list1.pop(list1.index(min(list1)))
    list2.pop(list2.index(min(list2)))
    total_distance += abs(min1 - min2)

print(total_distance)

