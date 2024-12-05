import re 

def check_mul(s):
    pattrn = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do()"
    dont_pattern = r"don't()"
    do_flag = 1
    dont_flag = 0 
    mulls = re.findall(pattrn,s)
    sum = 0
    for mul in mulls:
        sum += int(mul[0]) * int(mul[1])
    return sum
    

def seen_pats(s):
    pattrn = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    pattern_list = [pattrn,do_pattern,dont_pattern]
    seen = dict()
    
    final_sum = 0
    for pat in pattern_list:
        for match in  re.finditer(pat,s):
            seen[match.start()] = match.group()
    sorted_dict = {key: seen[key] for key in sorted(seen.keys())}

    flag = 1
    for key,value in sorted_dict.items():

        if(value[0] == 'm' and flag):
            match = re.match(pattrn, value)
            final_sum += int(match.groups(0)[0]) * int(match.groups(0)[1])
        elif("do()" in value):
            flag = 1
        elif("don't" in value):
            flag = 0

    return final_sum
        






def main():
    final_sum = 0
    with open("/Users/ganesh.ingale/adventofcode/Mull It Over/input.txt", "r", encoding="utf-8") as f:
        s = f.read()
        final_sum +=  seen_pats(s)
    
    print(final_sum)

    
    

if __name__ == "__main__":
    main()