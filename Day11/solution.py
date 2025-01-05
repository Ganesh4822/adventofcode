from functools import cache

@cache
def part_two(stone, counter):
    if counter == 75:
        return 1
    if stone == 0:
        return part_two(1,counter + 1)
    elif len(str(stone)) % 2 == 0:
        snum = str(stone)
        l = len(snum)
        return part_two(int(snum[:l //2]),counter + 1) + part_two(int(snum[l //2:]),counter + 1)
    else:
        return part_two(stone * 2024 , counter + 1)


def part_one(input):
    for _ in range(75):
        stones = []
        for num in input:
            if num == 0:
                stones.append(1)
            elif len(str(num)) % 2 == 0:
                snum = str(num)
                l = len(snum)
                stones.append(int(snum[:l //2]))
                stones.append(int(snum[l //2:]))
            else:
                stones.append(num * 2024)
        input = stones
    return len(input)



def main():
    #input = [[int(c) for c in line.split()] for line in open("/Users/ganesh.ingale/adventofcode/Day11/example.txt", "r", encoding="utf-8")]
    input = []
    with open("/Users/ganesh.ingale/adventofcode/Day11/example.txt", "r", encoding="utf-8") as f:
        for line in f:
            for c in line.split():
                input.append(int(c))
    # print(part_one(input))
    print(sum(part_two(i, 0) for i in input))
    #print(part_two(125,0))
        
if __name__ == "__main__":
    main()
