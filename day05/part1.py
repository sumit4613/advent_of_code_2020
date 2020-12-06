import argparse

"""\
F means "front",
B means "back",
L means "left",
R means "right".

Total -> range(0, 127)
F -> Lower Half -> range(0, 63)
B -> Upper Half -> range(63, 127)
"""


def compute(s: str) -> int:
    count = 0

    for line in s.splitlines():
        line = line.replace("F", "0").replace("B", "1")
        line = line.replace("R", "1").replace("L", "0")
        count = max(count, int(line, 2))
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
