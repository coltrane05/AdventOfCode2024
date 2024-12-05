
def is_x_mas(i, j, word_search):
    mas_count = 0
    dir_dict = {
        0 : [1, 1],
        1 : [1, -1],
        2 : [-1, 1],
        3 : [-1, -1],
    }
    
    for k in range(len(dir_dict)):
        dir_y = dir_dict[k][0]
        dir_x = dir_dict[k][1]
        i_1 = i + (dir_y * -1)
        j_1 = j + (dir_x * -1)
        mas_string = ""
        for l in range(0, 3):
            mas_string += word_search[i_1 + (dir_y * l)][j_1 + (dir_x * l)]

        if mas_string == "MAS":
            mas_count += 1

    if mas_count == 2:
        return True
    else:
        return False


word_search = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        line = line.replace("\n","")
        word_search.append(line)
        line = file.readline()


x_mas_count = 0
for i in range(1, len(word_search) - 1):
    for j in range(1, len(word_search[i]) - 1):
        if word_search[i][j] == "A" and is_x_mas(i, j, word_search):
            x_mas_count += 1
            

print(x_mas_count)