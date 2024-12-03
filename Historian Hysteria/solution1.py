
def findsimilarityScore(list1,list2):
    n = len(list1)
    seen = dict()
    score = 0
    for i in range(n):
        if list2[i] in seen:
            seen[list2[i]] += 1
        else:
            seen[list2[i]] = 1
    
    for i in range(n):
        if list1[i] in seen:
            score += list1[i] * seen[list1[i]]
    return score 
        



def findTotalDistance(list1,list2):
    sum = 0
    n1 = len(list1)
    n2 = len(list2)
    for i,j in zip(range(n1),range(n2)):
        sum += abs(list1[i] - list2[j])
    return sum

def main():
    arr1, arr2 = [], []
    with open("/Users/ganesh.ingale/adventofcode/Historian Hysteria/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            a, b = line.split()
            arr1.append(int(a))
            arr2.append(int(b))

    arr1.sort()
    arr2.sort()
    res = findTotalDistance(arr1,arr2)
    print(res)

    res2 = findsimilarityScore(arr1,arr2)
    print(res2)
    

if __name__ == "__main__":
    main()