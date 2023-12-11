with open('input.txt') as f:
    lines = f.readlines()
    nodes = {}
    for line in lines[2:]:
        nodes[line.split(" = ")[0]] = [line.split(" = (")[1].split(",")[0], line.split(" = (")[1].split(", ")[1][:-2]]
    inst = lines[0].strip()
    count = 0
    places = []
    ints = []
    slopes = []
    for key in nodes.keys():
        if key[-1] == "A":
            places.append(key)
            ints.append(0)
            slopes.append(0)
    while True:
        step = inst[count%len(inst)]
        for place in range(len(places)):
            if step == "R":
                places[place] = nodes[places[place]][1]
            else:
                places[place] = nodes[places[place]][0]
        count += 1
        flag = False
        print(places)
        for place in places:
            if(place[-1] != "Z"):
                pass
            else:
                pos = places.index(place)
                if(ints[pos] == 0):
                    ints[pos] = count
                elif(slopes[pos] == 0):
                    slopes[pos] = count - ints[pos]
        
        for slope in slopes:
            if slope == 0:
                flag = True
        if(not flag):
            print(count)
            break
    maxy = max(slopes)
    pos = slopes.index(maxy)
    c = 0
    print(slopes)
    print(ints)
    while True:
        c += 1
        check = maxy * pos + ints[pos]
        flag = False
        for slope in range(len(slopes)):
            if(check - ints[slope]) % slopes[slope] != 0:
                flag = True
                break
        if(not flag):
            print(check)
            break
        

        

