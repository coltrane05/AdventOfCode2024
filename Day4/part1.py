
def find_xmas(i, j, word_search, index_list):
    xmas_count = 0
    dir_dict = {
        0 : [-1, 0],
        1 : [-1, 1],
        2 : [0, 1],
        3 : [1, 1],
        4 : [1, 0],
        5 : [1, -1],
        6 : [0, -1],
        7 : [-1, -1]
    }
    
    for k in range(len(dir_dict)):
        dir_y = dir_dict[k][0]
        dir_x = dir_dict[k][1]
        xmas_string = "X"
        for l in range(1, 4):
            if (i + (dir_y * l)) < 0 or (j + (dir_x * l)) < 0:
                break
            try:
                xmas_string += word_search[i + (dir_y * l)][j + (dir_x * l)]
            except IndexError:
                break
            
        if xmas_string == "XMAS":
            xmas_count += 1

    return xmas_count


word_search = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        line = line.replace("\n","")
        word_search.append(line)
        line = file.readline()

index_list = []
xmas_count = 0

for i in range(len(word_search)):
    for j in range(len(word_search[i])):
        if word_search[i][j] == "X":
            xmas_count += find_xmas(i, j, word_search, index_list)

print(xmas_count)

