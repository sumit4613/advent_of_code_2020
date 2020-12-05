import argparse


def compute(s: str) -> int:
    lines = s.splitlines()
    x, y = 0, 0
    tree_count = 0
    x += 3
    x %= len(lines[0])
    y += 1
    while y < len(lines):
        if lines[y][x] == "#":
            tree_count += 1
        x += 3
        x %= len(lines[0])
        y += 1
    return tree_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())
