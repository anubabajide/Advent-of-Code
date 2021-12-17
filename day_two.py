from common import get_input
from collections import defaultdict

def find_final_postion(raw_directions):
    directions = defaultdict(int)
    for val in raw_directions:
        key, value = val.split(' ')
        directions[key] += int(value)
    return directions["forward"]*(directions["down"]-directions["up"])

def find_final_position_again(raw_directions):
    horizontal = depth = aim = 0
    for val in raw_directions:
        key, value = val.split(' ')
        value = int(value)
        if key == "forward":
            horizontal += value
            depth += aim*value
        elif key=="down":
            aim += value
        else:
            aim -= value
    return depth * horizontal

if __name__ == "__main__":
    raw = get_input("day_two.txt")
    print(find_final_postion(raw))
    print(find_final_position_again(raw))