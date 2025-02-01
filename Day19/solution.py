from functools import cache
path = "/Users/ganesh.ingale/adventofcode/Day19/input.txt"
patterns, designs = open(path, "r", encoding="utf-8").read().split("\n\n")
patterns = set(patterns.replace(", ", ",").strip().split(","))

max_pat_len = max(map(len,patterns))
designs = designs.split("\n")


cacheI = {}
def is_possible(design):
    if design ==  "": return True
    if design in cacheI: return cacheI[design]
    for i in range(min(len(design),max_pat_len) + 1):
        if design[:i] in patterns and is_possible(design[i:]):
            cacheI[design] = True
            return True
    cacheI[design] = False    
    return False

@cache
def part_two(design):
    if design == "": return 1
    count = 0
    for i in range(min(max_pat_len,len(design)) + 1):
        if design[:i] in patterns:
            count += part_two(design[i:])
    return count

def main():
    
    print(sum(1 if is_possible(design) else 0 for design in designs))
    print(sum(part_two(design) for design in designs))
    # for design in designs:
    #     print(design)
    #     flag = 0
    #     i = 0
    #     while i < len(design):
    #         if design[i] in patterns:
    #             print(design[i], "in pattern")
    #             i = i + 1
    #             continue
    #         else:
    #             print(design[i], "is not in pattern")
    #             j = 2
    #             while j <= len(design):
    #                 if design[i:i + j] not in patterns:
    #                     print(design[i:i + j], "not in pattern")
    #                     j = j + 1
    #                     flag  = 1
    #                 else:
    #                     print(design[i:i + j])
    #                     flag = 0
    #                     i = i + j 
    #                     break
    #         if flag == 1:
    #             break
    #     print(flag )
    #     if flag == 0:
    #         count = count + 1
    #     else:
    #         print(design,"is not possible")
    #     print("current count is " ,count)
    
if __name__ == "__main__":
    main()