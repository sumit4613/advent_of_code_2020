import argparse

"""\
F means "front",
B means "back",
L means "left",
R means "right".
"""


def compute(s: str) -> int:
    possible_set = set(range(1024))

    for line in s.splitlines():
        line = line.replace("F", "0").replace("B", "1")
        line = line.replace("R", "1").replace("L", "0")
        possible_set.discard(int(line, 2))

    for candidate in possible_set:
        if candidate - 1 not in possible_set and candidate + 1 not in possible_set:
            return candidate
    else:
        raise NotImplementedError("unreachable")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())
