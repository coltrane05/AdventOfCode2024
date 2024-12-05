

ordering_rules = {}
updates = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line != "\n":
        curr_rule = line.split()
        curr_rule = curr_rule[0].split("|")
        if curr_rule[0] not in ordering_rules:
            ordering_rules[curr_rule[0]] = [curr_rule[1]]
        else:
            ordering_rules[curr_rule[0]].append(curr_rule[1])
        
        line = file.readline()
    
    line = file.readline()
    while line:
        curr_page_nums = line.split()
        curr_page_nums = curr_page_nums[0].split(",")
        updates.append(curr_page_nums)
        line = file.readline()


correct_total = 0
for i in range(len(updates)):
    correct_order = True
    for j, e in reversed(list(enumerate(updates[i]))):
        if e in ordering_rules:
            if set(ordering_rules[e]) & set(updates[i][:j]):
                correct_order = False
    
    if correct_order:
        middle_index = len(updates[i]) // 2
        correct_total += int(updates[i][middle_index])

print(correct_total)