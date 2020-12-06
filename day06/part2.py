import argparse


def compute(s: str) -> int:
    count = 0
    for group in s.split("\n\n"):
        lines = group.splitlines()
        all_counted = set(lines[0])

        for other in lines[1:]:
            all_counted &= set(other)
        count += len(all_counted)
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
