import json

main_archive = {}

class Status():
    def __init__(self, index, gns, tn, archive):
        self.index = index
        self.greatest_num_steps = gns
        self.top_num = tn
        self.hailstone_archive = archive

status = Status(2, 1, 2, main_archive)

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
        if num in status.hailstone_archive:
            count = count + status.hailstone_archive[num]
            break
        elif num%2 == 0:
            hail_order.append(num)
            num = applyEven(num)
            count = count + 1
        else:
            hail_order.append(num)
            num = applyOdd(num)
            count = count + 1
    if not len(hail_order) == 0:
        for i in range(0,len(hail_order)):
            status.hailstone_archive[hail_order[i]] = count
    return count

print("Q to quite and save dictionary to file in data directory")

def loop():
    while(True):
        count = analyze(status.index)
        if(count > status.greatest_num_steps):
            status.greatest_num_steps = count
            status.top_num = status.index
            print("Num: ", status.top_num, ", Steps: ", status.greatest_num_steps)
        status.index = status.index + 1

def main():
    try:
        loop()
    except KeyboardInterrupt:
        Uin = input("Enter a command (q to quit and d to show dict length and continue): ")
        if(Uin == "q"):
            pass
        elif(Uin == "d"):
            print(len(status.hailstone_archive))
            UinPrime = input("Continue (Y/N): ")
            if(UinPrime == "Y"):
                main()
            else:
                pass

main()


main_input = input("Would you like to save the hailstone_dictionary that was created? (Y/N): ")

if(main_input == "Y"):
    print("Saving dictionary to data directory...")

    #save data
    with open('data/data.json', 'w') as fp:
        json.dump(status.hailstone_archive, fp)

    print("Data saved.")
else:
    print("Done")
