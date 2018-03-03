def isEven(num):
    if(num%2 == 0):
        return True
    else:
        return False

def applyOdd(num):
    return 3*num + 1

def applyEven(num):
    return num/2

def analyze(num, count):
    if(isEven(num)):
        num = applyEven(num)
    else:
        num = applyOdd(num)
    if(num == 1):
        print("Value: ", num, "Iteration: ", count)
        return count
    else:
        print("Value: ", num, "Iteration: ", count)
        analyze(num, count+1)

num = input("Please enter a number to test the hailstone conjecture: ")
analyze(int(num), 1)
