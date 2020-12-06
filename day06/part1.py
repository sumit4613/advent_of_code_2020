import argparse


def naive_compute(s: str) -> int:
    count = 0
    for a in s.split("\n\n"):
        a = a.replace("\n", "")
        count += len(set(a))

    return count


def compute(s: str) -> int:
    count = 0
    for line in s.split("\n\n"):
        count += len(set(line) - {" ", "\n"})
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
