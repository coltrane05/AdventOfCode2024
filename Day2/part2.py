

safe_total = 0

def check_safety(report) -> bool:
    safe = True
    direction = None
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if diff == 0:
            safe = False
            break

        if abs(diff) > 3:
                safe = False
                break

        if direction == None:
            if diff > 0:
                direction = "increasing"
            elif diff < 0:
                direction = "decreasing"
        else:
            if diff > 0 and direction == "decreasing":
                safe = False
                break
            if diff < 0 and direction == "increasing":
                safe = False
                break

    return safe


with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        string_report = line.split()
        int_report = [int(x) for x in string_report]
        
        if (
            check_safety(int_report)

            or any(
                check_safety(int_report[:i] + int_report[i + 1:])
                for i in range(len(int_report))
            )
        ):
            safe_total += 1
        line = file.readline()

print(safe_total)
        

                    



