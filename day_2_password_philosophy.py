with open("Inputs/day_2.txt") as input_:
    passwords = input_.readlines()
    passwords = [line.replace("\n", "") for line in passwords]
    print(f"There are {len(passwords)} total passwords")


def parse_part_one():
    for password in passwords:
        separated = password.split(":")  # rule: password
        rule = separated[0].split(" ")
        rule_amount = rule[0].split("-")  # 1-3 a: abcde
        # this retrieves [1, 3]
        letter = rule[1]
        password = separated[1]
        rule_amount = range(int(rule_amount[0]), int(rule_amount[1]) + 1)  # add 1 because python range function
        # range(1, 3) does not include 3, but we need it to
        yield test_part_one(password, letter, rule_amount)


def test_part_one(password, letter, amount):
    counter = 0
    for character in password:
        if character == letter:
            counter += 1
    return counter in amount  # amount is always going to be a range object


def parse_part_two():
    for password in passwords:
        separated = password.split(":")  # rule: password
        rule = separated[0].split(" ")
        rule_amount = rule[0].split("-")  # 1-3 a: abcde
        rule_amount = [int(number) for number in rule_amount]
        # this retrieves [1, 3]
        letter = rule[1]
        password = separated[1]
        yield test_part_two(password, letter, rule_amount)


def test_part_two(password, letter, positions):
    count = 0
    for position, character in enumerate(password):
        if character == letter:
            if position in positions:
                count += 1
    return count == 1


if __name__ == "__main__":
    true = 0
    false = 0
    for result in parse_part_one():
        if result:
            true += 1
        else:
            false += 1
    print(f"{true} passwords are valid, while {false} passwords are not")
    print("-" * 10)
    true = 0
    false = 0
    for result in parse_part_two():
        if result:
            true += 1
        else:
            false += 1
    print(f"{true} passwords are valid, while {false} passwords are not")
