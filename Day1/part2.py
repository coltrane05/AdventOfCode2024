list1 = []
list2 = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        line_split = line.split()
        list1.append(int(line_split[0]))
        list2.append(int(line_split[1]))
        line = file.readline()


totalSimilarity = 0
# while list1:
#     min1 = min(list1)
#     min2 = min(list2)
#     list1.pop(list1.index(min(list1)))
#     list2.pop(list2.index(min(list2)))
#     totalDistance += abs(min1 - min2)

for i in range(len(list1)):
    totalSimilarity += list1[i] * list2.count(list1[i])

print(totalSimilarity)