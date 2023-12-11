seeds = []
with open("input.txt") as f:
    lines = f.readlines()
    seeds = [int(x) for x in lines[0].split(":")[1].strip().replace("  ", " ").split(" ")]
    maps = []
    for line in lines[1:]:
        if(line.strip() == ""):
            maps.append([])
        else:
            maps[-1].append(line.strip().replace("  ", " ").split(" "))
    maps = [[[int(j) for j in y] for y in x[1:]] for  x in maps]
    this = []
    for seed in range(0, len(seeds), 2):
        this.append([seeds[seed], seeds[seed + 1]])
    for mapy in maps:
        new = []
        for place in range(0, len(this)): 
            covered = []
            for row in mapy:
                if(row[1] <= this[place][0] <= row[1] + row[2]):
                    new.append([row[0] - row[1] + this[place][0], min(this[place][1], row[1] + row[2] - this[place][0])])
                    covered.append([this[place][0], min(this[place][1], row[1] + row[2] - this[place][0])])
                elif(row[1] <= this[place][1] + this[place][0] <= row[1] + row[2]):
                    new.append([row[0], this[place][1] + this[place][0] - row[1]])
                    covered.append([row[1], this[place][1] + this[place][0] - row[1]])
                elif(this[place][0] <= row[1] <= this[place][0] + this[place][1]):
                    new.append([row[0], row[2]])
                    covered.append([row[1], row[2]])
            covered.sort()
            if(len(covered) == 0):
                new.append([this[place][0], this[place][1]])
                continue
            elif(covered[0][0] > this[place][0]):
                new.append([this[place][0], min(this[place][1], covered[0][0] - this[place][0])])
            for i in range(0, len(covered) - 1):
                if(covered[i + 1][0] > covered[i][0] + covered[i][1] + 1):
                    new.append([covered[i][0] + covered[i][1], covered[i + 1][0] - covered[i][0] - covered[i][1]])
            if(covered[-1][0] + covered[-1][1] < this[place][0] + this[place][1]):
                new.append([covered[-1][0] + covered[-1][1], this[place][0] + this[place][1] - covered[-1][0] - covered[-1][1]])
                
        this = new.copy()
    print(this)
    print(min(this))
            
                
