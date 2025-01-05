def check_safe_pages(rules,pages):
    sum = 0
    for page in pages:
        flag = 1
        for i,single in reversed(list(enumerate(page))):
            rule = rules[str(single)]
            for j in range(i):
                if int(page[j]) in rule:
                    flag = 0
                    break
                if flag == 0:
                    break
            
        if flag == 1:
            middle = int((len(page)-1)/2)
            #print(page[middle])
            sum += int(page[middle])
    return sum


def check(rules,page):
    for i,single in reversed(list(enumerate(page))):
        rule = rules[str(single)]
        for j in range(i):
            if(int(page[j])) in rule:
                return 0

    middle = int((len(page)-1)/2)
    return int(page[middle])    

def fix(rules,page):
    checker = 0
    flag = True
    while flag:
        for i,single in reversed(list(enumerate(page))):
            rule = rules[str(single)]
            for j in range(i):
                if int(page[j]) in rule:
                    page.append(page.pop(j))
                    break

            checker = check(rules,page)
            if checker > 0:
                return checker    

def check_safe_pages_part2(rules,pages):
    
    incorrect_pages = []
    for page in pages:
        flag = 1
        for i,single in reversed(list(enumerate(page))):
            rule = rules[str(single)]
            for j in range(i):
                if int(page[j]) in rule:
                    flag = 0
                    break
                if flag == 0:
                    break
            
        if flag == 0:
            incorrect_pages.append(page)

    checkSum = 0
    for page in incorrect_pages:
        
        checkSum += fix(rules,page)
        # for i,value in reversed(list(enumerate(page))):
            # rule = rules[str(value)]
            # for j in range(i):
            #     if int(page[j]) in rule:
       

            
    return checkSum

            
def main(): 
    rules = {}
    pages = []
    sum = 0
    #string : [int array]
    with open("/Users/ganesh.ingale/adventofcode/Print Queue/input.txt", "r", encoding="utf-8") as f:
        flag = False
        for line in f:
            
            line = line.strip()
            if line == "":
                flag = True
                continue

            if not flag: 
                nums = line.split('|')
                num = int(nums[1])
                if nums[0] not in rules:
                    rules[nums[0]] = [num]
                else:
                    rules[nums[0]].append(num)
            else:
                page = line.split(',')
                pages.append(page)
    #print(rules)  
    #print(pages)      
    sum = check_safe_pages_part2(rules,pages)

    print(sum)







            
if __name__ == "__main__":
    main()