import re
import itertools

def check2(target,digits):
    operators2 = ['*', '+', '||']
    operator_combos = list(itertools.product(operators2,repeat = len(digits)-1))
    
    for ops in operator_combos:
        result = digits[0]
        #expression = "".join(str(digits[i]) + ops[i] for i in range(len(ops))) + str(digits[-1])
        for i in range(len(ops)):
            if ops[i] == '+':
                result += digits[i+1]
            elif ops[i] == '*':
                result *= digits[i+1]
            elif ops[i] == '||':
                result = int(str(result) + str(digits[i+1]))
        if result == target:
            return target
    return 0
        



def check(target,digits):
    #combinations = 2 ** (len(digits) - 1)
    operators = ['*', '+']
    operators2 = ['*', '+', '||']
    operators_combos = list(itertools.product(operators,repeat = len(digits)-1))
    print(operators_combos)
    for ops in operators_combos:
        result = digits[0]
        #expression = "".join(str(digits[i]) + ops[i] for i in range(len(ops))) + str(digits[-1])
        for  i in range(len(ops)):
            if ops[i] == '+':
                result += digits[i + 1]
            elif ops[i] == '*':
                result *= digits[i+1]
        if result == target:
            return target
    return 0   

def part_one(values):
    sum = 0
    for target,digits in values.values():
        sum += check(target,digits)
    return sum


def part_two(values):
    sum = 0 
    
    for target,digits in values.values():
        sum += check2(target,digits)
    return sum

def main(): 
    values = {}
    with open("/Users/ganesh.ingale/adventofcode/Day7/example.txt", "r", encoding="utf-8") as f:
        i = 0
        for line in f:
            numbers = re.findall(r'\d+', line)
            digits = [int(y) for y in numbers]
            target = digits.pop(0)

            values[i] = [target,digits]
            i = i + 1
    print(values)
    sum = 0    
    sum = part_two(values)  
    print(sum)  

            
if __name__ == "__main__":
    main()

