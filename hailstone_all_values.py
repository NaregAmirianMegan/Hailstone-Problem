hailstone_archive = {}

def isEven(num):
    if(num%2 == 0):
        return True
    else:
        return False

def applyOdd(num):
    return 3*num + 1

def applyEven(num):
    return num/2

def analyze(num):
    count = 0
    hail_order = []
    while(num != 1):
        if num in hailstone_archive:
            count = count + hailstone_archive[num]
            break
        elif num%2 == 0:
            num = applyEven(num)
            count = count + 1
        else:
            num = applyOdd(num)
            count = count + 1
    if not len(hail_order) == 0:
        for i in range(0,len(hail_order)):
            hailstone_archive[hail_order[i]] = count
    return count

index = 2
greatest_num_steps = 1
top_num = 2

#for now use control-c to break loop
while(True):
    count = analyze(index)
    if(count > greatest_num_steps):
        greatest_num_steps = count
        top_num = index
        print(greatest_num_steps, ", ", top_num)
    index = index + 1
