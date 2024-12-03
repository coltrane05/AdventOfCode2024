input_read = 0
index = 0
num_1 = ""
num_2 = ""

def start(input):
    global input_read
    global index
    global num_1
    global num_2
    input_read = 0
    index = 0
    num_1 = ""
    num_2 = ""
    S0(input)
    return input_read

def S0(input):
    global input_read
    global index
    if input[index] == 'm':
        input_read += 1
        index += 1
        S1(input)
    else:
        Serr()

def S1(input):
    global input_read
    global index
    if input[index] == 'u':
        input_read += 1
        index += 1
        S2(input)
    else:
        Serr()

def S2(input):
    global input_read
    global index
    if input[index] == 'l':
        input_read += 1
        index += 1
        S3(input)
    else:
        Serr()

def S3(input):
    global input_read
    global index
    if input[index] == '(':
        input_read += 1
        index += 1
        S4(input)
    else:
        Serr()
    
def S4(input):
    global input_read
    global index
    global num_1
    global num_2
    if input[index].isdigit():
        num_1 += input[index]
        input_read += 1
        index += 1
        if input[index].isdigit():
            S4(input)
        else:
            S5(input)
    else:
        Serr()

def S5(input):
    global input_read
    global index
    if input[index] == ',':
        input_read += 1
        index += 1
        S6(input)
    else:
        Serr()

def S6(input):
    global input_read
    global index
    global num_1
    global num_2
    if input[index].isdigit():
        num_2 += input[index]
        input_read += 1
        index += 1
        if input[index].isdigit():
            S6(input)
        else:
            S7(input)
    else:
        Serr()

def S7(input):
    global input_read
    global index
    if input[index] == ')':
        input_read += 1
        index += 1
    else:
        Serr()

def Serr():
    global input_read
    input_read = 0

puzzle_input = ""
with open("input.txt", "r") as file:
    puzzle_input = file.read()


multiplication_results = 0
while puzzle_input != "":
    if start(puzzle_input) >= 8:
        multiplication_results += (int(num_1) * int(num_2))
        puzzle_input = puzzle_input[8:]
    else:
        puzzle_input = puzzle_input[1:]

print(multiplication_results)    

