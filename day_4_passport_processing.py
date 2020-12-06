import re


class Passport:
    def __init__(self, data):  # attributes all from question
        self.parsed = parse(data)
        self.byr = self.parsed.get("byr")
        self.iyr = self.parsed.get("iyr")
        self.eyr = self.parsed.get("eyr")
        self.hgt = self.parsed.get("hgt")
        self.hcl = self.parsed.get("hcl")
        self.ecl = self.parsed.get("ecl")
        self.pid = self.parsed.get("pid")
        self.cid = self.parsed.get("cid")
        self.valid_part_one = self.check_part_one()
        self.valid_part_two = self.check_part_two()

    def check_part_one(self):
        return not None in [self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid]

    def check_part_two(self):  # all rules given by question
        if not self.valid_part_one: return False  # if it's missing something other than cid, it's automatically invalid
        if len(str(self.byr)) != 4 or (not 1920 <= int(self.byr) <= 2002): return False
        if len(str(self.iyr)) != 4 or (not 2010 <= int(self.iyr) <= 2020): return False
        if len(str(self.eyr)) != 4 or (not 2020 <= int(self.eyr) <= 2030): return False
        if not (str(self.hgt).endswith("cm") or str(self.hgt).endswith("in")): return False
        else:
            height = int(self.hgt[:-2])
            if self.hgt[-2:] == "cm":
                if not (150 <= height <= 193): return False
            if self.hgt[-2:] == "in":
                if not (59 <= height <= 76): return False
        if not self.hcl.startswith("#") or (len(re.findall(r"[a-f0-9]", self.hcl)) != 6): return False  # amount of
        # characters a-f or 0-9
        if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False
        if len(str(self.pid)) != 9: return False
        return True


def parse(string):
    string = string.split(" ")  # each attribute separated by a space
    data = {}
    for entry in string:
        set_ = entry.split(":")  # attribute:value
        name = set_[0]
        value = set_[1]
        data[name] = value
    return data


def join_(list_):  # join the lines of the file together by each passport entry
    joined = []
    for entry in list_:
        if not bool(joined) or not bool(entry):  # not bool(joined) only pertains to the very first line
            # if an empty line is encountered it means there is a new entry
            # it is ok if it appends an empty string because the else: will make it add to the end of an empty string
            # which brings no effect
            joined.append(entry)
        else:
            joined[-1] += entry if joined[-1] == "" else " " + entry  # add a space if not at the beginning of a new
            # entry
    return joined


with open("Inputs/day_4.txt") as input_:
    passports = input_.read()
    passports = passports.split("\n")
    passports = join_(passports)

if __name__ == "__main__":
    passports = [Passport(passport) for passport in passports]
    valid_part_one = [passport for passport in passports if passport.valid_part_one]
    print(f"There are {len(valid_part_one)} valid passports")
    print("-" * 10)
    valid_part_two = [passport for passport in passports if passport.valid_part_two]
    print(f"There are {len(valid_part_two)} valid passports")
