

def check(stri, dict):
    cards = stri.split(" ")[0]
    face = ['T', "Q", "K", "A"]
    arr = []
    for x in range(13):
        arr.append(0)
    for card in cards:
        if card.isdigit():
            arr[int(card) - 2] += 1
        elif card in face:
            arr[face.index(card) + 8] += 1
    arr.sort()
    for card in cards:
        if card == "J":
            arr[-1] += 1
    print(stri, arr)
    stri = stri.replace("T", "B")
    stri = stri.replace("J", "1")
    stri = stri.replace("Q", "D")
    stri = stri.replace("K", "E")
    stri =stri.replace("A", "F")
    arr[0] += 1;
    if(arr[-1] == 5):
        dict[7].append(stri)
    elif(arr[-1] == 4):
        dict[6].append(stri)
    elif(arr[-1] == 3 and arr[-2] == 2):
        dict[5].append(stri)
    elif(arr[-1] == 3):
        dict[4].append(stri)
    elif(arr[-1] == 2 and arr[-2] == 2):
        dict[3].append(stri)
    elif(arr[-1] == 2):
        dict[2].append(stri)
    else:
        dict[1].append(stri)
    
    return dict 
        

with open("input.txt") as f:
    lines = f.readlines()
    types = {}
    types[0] = []
    types[1] = []
    types[2] = []
    types[3] = []
    types[4] = []
    types[5] = []
    types[6] = []
    types[7] = []
    for line in lines:
        types = check(line.strip(), types)
    for i in types:
        types[i].sort()
    print(types)
    
    count = 1
    total = 0
    for i in types:
        for j in types[i]:
            total += count * int(j.split(" ")[1].strip())
            count += 1
    print(total)
        

    


