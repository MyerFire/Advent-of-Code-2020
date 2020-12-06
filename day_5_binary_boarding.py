class BoardingPass:
    def __init__(self, data):
        self.row, self.column, self.id = parse(data)  # returns tuple


def parse(data):
    row_specification = data[:7]  # first seven characters
    column_specification = data[-3:]  # last three characters
    row = list(range(0, 128))  # total of 128 rows on the plane
    column = list(range(0, 8))  # total of 8 columns on the plane
    for character in row_specification:
        if character == "F":
            row = row[:len(row) // 2]  # first half
        if character == "B":
            row = row[len(row) // 2:]  # second half
    for character in column_specification:
        if character == "L":
            column = column[:len(column) // 2]  # first half
        elif character == "R":
            column = column[len(column) // 2:]  # second half
    id_ = row[0] * 8 + column[0]  # this id formula is provided by the question
    return row[0], column[0], id_


def sort_key(boarding_pass):  # key for sort function later
    return boarding_pass.id


with open("Inputs/day_5.txt") as input_:
    boarding_passes = input_.readlines()
    boarding_passes = [boarding_pass.replace("\n", "") for boarding_pass in boarding_passes]

if __name__ == "__main__":
    boarding_passes = [BoardingPass(boarding_pass) for boarding_pass in boarding_passes]
    boarding_passes.sort(key=sort_key, reverse=True)
    print(f"{boarding_passes[0].id} is the highest seat ID")
    print("-" * 10)
    for index, boarding_pass in enumerate(boarding_passes):
        if index == 0:
            pass
        else:
            if boarding_pass.id + 1 != boarding_passes[index - 1].id:  # gap between the pattern of numbers
                print(f"There is a missing seat between seat ID {boarding_pass.id} and {boarding_passes[index - 1].id}"
                      f", which is {(boarding_pass.id + boarding_passes[index - 1].id) // 2}")  # gets the average
                # (number in the middle)
