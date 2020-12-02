with open("Inputs/day_1.txt") as input_:
    report = input_.readlines()
    report = [int(line.replace("\n", "")) for line in report]


def part_one():
    for number in report:
        for number_ in report:
            if number + number_ == 2020:
                return number, number_


def part_two():
    for number in report:
        for number_ in report:
            for number__ in report:
                if number + number_ + number__ == 2020:
                    return number, number_, number__


if __name__ == "__main__":
    result_one, result_two = part_one()
    print(f"The two numbers are {result_one} and {result_two}")
    print(f"The product of the two numbers is {result_one * result_two}")
    print("-" * 10)
    result_three, result_four, result_five = part_two()
    print(f"The three numbers are {result_three}, {result_four}, {result_five}")
    print(f"The product of the two numbers is {result_three * result_four * result_five}")
