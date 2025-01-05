


def isIncreasing(list1):
    n = len(list1)
    for i in range(n - 1):
        if(int(list1[i+1]) < int(list1[i])):
            return False
    return True

def isDecreasing(list1):
    n = len(list1)
    for i in range(n - 1):
        if(int(list1[i+1]) > int(list1[i])):
            return False
    return True


def isReportsafe(list1):
    n = len(list1)
    flag = 1
    if(not(isIncreasing(list1) or isDecreasing(list1))):
        return 0
    for i in range(1,n):
        if((abs(int(list1[i]) - int(list1[i-1])) < 1) or (abs(int(list1[i]) - int(list1[i-1])) > 3)):
            return 0
    return 1

        
def isReportDampenersafe(list1):
    n = len(list1)
    for i in range (n):
        if (isReportsafe(list1[:i] + list1[i+1:])):
           return 1
    return 0
     
        

def main():
    count = 0
    with open("/Users/ganesh.ingale/adventofcode/p2/input.txt", "r") as f:
        for line in f:
            list1 = line.split()
            count += isReportDampenersafe(list1)
    print(count)

    
            
if __name__ == "__main__":
    main()            
    