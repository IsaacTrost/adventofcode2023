with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in range(len(lines)):
        for char in range(len(lines[line])):
            if lines[line][char] == "S":
                start = (line, char)
                break
    
    if(lines[start[0] + 1][start[1]] == "|" or lines[start[0] + 1][start[1]] == "7" or lines[start[0] + 1][start[1]] == "F"):
        loc = [start[0] + 1, start[1]]
    elif(lines[start[0] - 1][start[1]] == "|" or lines[start[0] - 1][start[1]] == "J" or lines[start[0] - 1][start[1]] == "L"):
        loc = [start[0] - 1, start[1]]
    else:
        loc = [start[0], start[1] + 1]
    prev = start
    total = 1
    while(lines[loc[0]][loc[1]] != "S"):
        temp = loc.copy()
        if(lines[loc[0]][loc[1]] == "|"):
            if(loc[0] > prev[0]):
                loc[0] += 1
            elif(loc[0] < prev[0]):
                loc[0] -= 1
        elif(lines[loc[0]][loc[1]] == "-"):
            if(loc[1] > prev[1]):
                loc[1] += 1
            elif(loc[1] < prev[1]):
                loc[1] -= 1
        elif(lines[loc[0]][loc[1]] == "L"):
            if(loc[0] == prev[0]):
                loc[0] -= 1
            else:
                loc[1] += 1
        elif(lines[loc[0]][loc[1]] == "J"):
            if(loc[0] == prev[0]):
                loc[0] -= 1
            else:
                loc[1] -= 1
        elif(lines[loc[0]][loc[1]] == "7"):
            if(loc[0] == prev[0]):
                loc[0] += 1
            else:
                loc[1] -= 1
        elif(lines[loc[0]][loc[1]] == "F"):
            if(loc[0] == prev[0]):
                loc[0] += 1
            else:
                loc[1] += 1
        else:
            print("Error", loc)
            break
        total += 1
        prev = temp

    print(total//2)