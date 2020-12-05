import argparse

"""\
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

REQUIRED = frozenset(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))


def compute(s: str) -> int:
    count = 0
    for passport in s.split("\n\n"):
        split_fields = [s.strip().split(":", 1) for s in passport.split()]
        fields = {k: v for k, v in split_fields}
        if fields.keys() >= REQUIRED:
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
