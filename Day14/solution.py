import re


# This questions can be solved by distance formula which is d = start + v * t 
# to calculate the final positions we can take the remainder d  %  bound





def find_quadrant(x,y,xl,yl):
    if x < int(xl / 2) and y < int(yl / 2):
        return 1
    elif x > int(xl / 2) and y < int(yl / 2):
        return 2
    elif x < int(xl / 2) and y > int(yl / 2):
        return 3
    elif x > int(xl / 2) and y > int(yl / 2):
        return 4
    return 0



def part_one(path,xl,yl,repeats):
    final_positions = dict()
    score = 1
    for line in open(path,"r",encoding="utf-8").read().split("\n"):
        sx,sy,x,y = map(int,re.findall(r"[-+]?\d+",line))
        X = sx + repeats * x
        Y = sy + repeats * y
        fx = X % xl
        fy = Y % yl
        q = find_quadrant(fx,fy,xl,yl)
        if q in final_positions:
            final_positions[q] += 1
        else:
            final_positions[q] = 1
    
    for q,count in final_positions.items():
        if q != 0:
            score *= count
    
    return score



def part_two(path,xl,yl):
    
    
    min_safety = float("inf")
    iteration = 0
    for repeats in range(xl * yl):
        score = 1
        final_positions = dict()
        for line in open(path,"r",encoding="utf-8").read().split("\n"):
            sx,sy,x,y = map(int,re.findall(r"[-+]?\d+",line))
            X = sx + repeats * x
            Y = sy + repeats * y
            fx = X % xl
            fy = Y % yl
            q = find_quadrant(fx,fy,xl,yl)
            if q in final_positions:
                final_positions[q] += 1
            else:
                final_positions[q] = 1
    
        for q,count in final_positions.items():
            if q != 0:
                score *= count
        if score < min_safety:
            min_safety = score
            iteration = repeats
        
    return iteration



    


    


def main():
    path = "/Users/ganesh.ingale/adventofcode/Day14/input.txt"
    # print(part_one(path,11,7,100))
    print(part_two(path,101,103))
    


if __name__ == "__main__":
    main()