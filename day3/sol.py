from curses.ascii import isdigit

def soround(lines, x, y, dicty):
    total = 0
    place = y
    while(lines[x][place].isdigit()):
        
        total*=10
        total+=int(lines[x][place])
        place+=1
    for i in range(max(0, x-1), min(x+2, len(lines))):
        for j in range(max(0, y-1), min(place+1, len(lines[i]))):
            if(lines[i][j] != '.' and lines[i][j] != '\n' and not lines[i][j].isdigit()):
                if(lines[i][j] == "*"):
                    if (i, j) in dicty:
                        dicty[(i, j)].append(total)
                    else:
                        dicty[(i, j)] = [total]
                return total, place - y
    # print(total)
    return 0, place - y
    
with open('input.txt', 'r') as f:
    total = 0
    lines = f.readlines()
    dicty = {}
    for line in range(len(lines)):
        flag = False
        char = 0
        while char < len(lines[line]):
            if(lines[line][char].isdigit()):
                bump, add = soround(lines, line, char, dicty)
                total += bump
                char += add
            char+=1
    parttwo = 0
    for elem in dicty:
        if(len(dicty[elem]) == 2):
            parttwo += dicty[elem][0] * dicty[elem][1]
print('part 1', total)
print('part 2', parttwo)
