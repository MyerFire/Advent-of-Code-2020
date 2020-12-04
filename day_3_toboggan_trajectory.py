with open("Inputs/day_3.txt") as input_:
    map_ = input_.readlines()
    map_ = [line.replace("\n", "") for line in map_]


def part_one():
    x = 0
    y = 0
    for _ in map_:
        yield get_position(x, y)
        x += 3
        y += 1


def part_two_structure(x_slope, y_slope):
    x = 0
    y = 0
    for _ in map_:
        if y > len(map_):
            return  # we're done if the y goes over the amount of actual y axis points there are
        yield get_position(x, y)
        x += x_slope
        y += y_slope


def get_position(x, y):
    while x >= len(map_[y]):  # since the pattern repeats itself, just count backwards
        x = x - len(map_[y])
    return map_[y][x]  # y line (down) x character (right)


if __name__ == "__main__":
    path = [space for space in part_one()]
    trees = path.count("#")
    print(f"There are {trees} trees on this path")
    print("-" * 10)
    trees = []
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )
    for slope in slopes:
        path = [space for space in part_two_structure(slope[0], slope[1])]
        trees.append(path.count("#"))
    trees_product = 1
    for number in trees:
        trees_product *= number  # numpy overflows here so like whatever
    print(f"The product of the number of trees on these paths is {trees_product}")
