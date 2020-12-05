import argparse
from typing import List


def compute_slope(lines: List[str], r_move: int, d_move: int) -> int:
    x, y = 0, 0
    tree_count = 0
    x += r_move
    x %= len(lines[0])
    y += d_move
    while y < len(lines):
        if lines[y][x] == "#":
            tree_count += 1
        x += r_move
        x %= len(lines[0])
        y += d_move
    return tree_count


def compute(s: str) -> int:
    lines = s.splitlines()

    return (
        compute_slope(lines, 1, 1)
        * compute_slope(lines, 3, 1)
        * compute_slope(lines, 5, 1)
        * compute_slope(lines, 7, 1)
        * compute_slope(lines, 1, 2)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())
