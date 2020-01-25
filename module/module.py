__counter = 0

def sum1(list):
    global __counter
    __counter += 1
    sum = 0
    for e in list:
        sum += e
    return sum

def prod1(list):
    global __counter
    __counter += 1
    prod = 1
    for e in list:
        prod *= e
    return prod
    

if __name__ == "__main__":
    print("I prefer to be a module")
    l=[i+1 for i in range (5)]
    print(sum1(l) ==15)
    print(prod1(l) ==120)

