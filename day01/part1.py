import argparse


def naive_compute(s: str) -> int:
    """Naive Approach"""
    inputs = list(s.split())
    for i in range(len(inputs)):
        for j in range(i, len(inputs)):
            if int(inputs[i]) + int(inputs[j]) == 2020:
                return int(inputs[i]) * int(inputs[j])
    else:
        raise NotImplementedError


def compute(s: str) -> int:
    """Better Approach than naive_compute"""
    numbers = set()
    for n_str in s.split():
        n = int(n_str)
        numbers.add(n)
        if 2020 - n in numbers:
            return (2020 - n) * n
    else:
        raise NotImplementedError


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())
