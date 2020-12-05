import argparse
import re

"""\
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""

REQUIRED = frozenset(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))


def compute(s: str) -> int:
    count = 0
    for passport in s.split("\n\n"):
        split_fields = [s.strip().split(":", 1) for s in passport.split()]
        fields = {k: v for k, v in split_fields}
        if (
            fields.keys() >= REQUIRED
            and 1920 <= int(fields["byr"]) <= 2002
            and 2010 <= int(fields["iyr"]) <= 2020
            and 2020 <= int(fields["eyr"]) <= 2030
            and (m1 := re.match(r"^(\d+)(cm|in)$", fields["hgt"]))
            and (
                m1[2] == "cm"
                and 150 <= int(m1[1]) <= 193
                or m1[2] == "in"
                and 59 <= int(m1[1]) <= 76
            )
            and re.match("^#[a-f0-9]{6}$", fields["hcl"])
            and fields["ecl"] in set("amb blu brn gry grn hzl oth".split())
            and re.match("^[0-9]{9}$", fields["pid"])
        ):
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())
