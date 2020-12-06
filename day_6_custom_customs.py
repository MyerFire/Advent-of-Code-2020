def join(list_):  # since every group is separated by a newline, processing is needed to separate newlines between
    # groups and newlines between people of a group
    joined = []
    for entry in list_:
        if not bool(joined) and bool(entry):  # first line
            joined.append([entry])
        elif not bool(entry):  # basically if entry == "":
            joined.append([])
        else:
            joined[-1].append(entry)
    return joined


def parse_part_one(group):
    counts = {}  # this way of doing things gets the amount of times the character appears in the string as well
    for person in group:
        for character in person:
            if not counts.get(character):
                counts[character] = 1
            else:  # if it exists already, then just increment by one; this makes it so that the amount of entries
                # in the dict will be the amount of unique characters (the goal), and also gets the count
                counts[character] += 1
    return counts


def parse_part_two(group):
    counts = parse_part_one(group)  # first part is usable in second part
    all_yes = 0
    for key, value in counts.items():
        if value == len(group):  # if a question was answered "yes" to the same number of times as the people in the
            # group
            all_yes += 1
    return all_yes


with open("Inputs/day_6.txt") as input_:
    data = input_.readlines()
    data = [group.replace("\n", "") for group in data]
    data = join(data)

if __name__ == "__main__":
    total = 0
    for group in data:
        total += len(parse_part_one(group))
    print(f"The total amount of questions people answered \"yes\" to is {total}")
    print("-" * 10)
    total = 0
    for group in data:
        total += parse_part_two(group)
    print(f"The total amount of questions every person in a group answered \"yes\" to is {total}")