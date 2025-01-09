import re


# This question is basically solving a linear equation

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# For above example we will need few A button presses and few B button presses and the final point that we want to reach is X  = 84000 and Y = 5400
# A button moves 94 point on x axis and B moves 22 point B axis hence to get exact number of button press we can represnt A and B button presses \
# 94A + 22B = 8400
# and similarly for Y coordinate 
# 34A + 67B = 5400

# axA + bxB = c1
# ayA + byB = c2

# axbyA + bxbyB = c1by
# aybxA + bxbyB = c2bx

# solving above equation we get 

# A(axby - aybx) = (c1by - c2bx)
# A = (c1by - c2bx) / (axby - aybx)

# c1 - ax((c1by - c2bx) / (axby - aybx)) / bx  = B
# c1 - ax(A) / bx  = B





def part_one(path):
    total = 0
    for block in  open(path, "r", encoding="utf-8").read().split("\n\n"):
        ax , ay , bx, by , c1 , c2 = map(int, re.findall(r"\d+",block))
        #part2
        c1 += 10000000000000
        c2 += 10000000000000
        A = (c1*by - c2*bx) / (ax*by - ay*bx)
        B = (c1 - ax*A) / bx
        if A % 1 == 0 and B % 1 == 0:
            total += int(A * 3 + B)
    return total

def main():

    path = "/Users/ganesh.ingale/adventofcode/Day13/input.txt"
    
    print(part_one(path))
    

    

if __name__ == "__main__":
    main()