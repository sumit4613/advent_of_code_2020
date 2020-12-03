import argparse
import itertools


def naive_compute(s: str) -> int:
    """Naive Approach"""
    inputs = list(s.split())
    for i in range(len(inputs)):
        for j in range(i, len(inputs)):
            for k in range(i, len(inputs)):
                if int(inputs[i]) + int(inputs[j]) + int(inputs[k]) == 2020:
                    return int(inputs[i]) * int(inputs[j]) * int(inputs[k])
    else:
        raise NotImplementedError


def compute(s: str) -> int:
    """Better Approach than naive_compute"""
    numbers = [int(n_str) for n_str in s.split()]
    for a, b, c in itertools.combinations(numbers, 3):
        if a + b + c == 2020:
            return a * b * c
    else:
        raise NotImplementedError


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        # change compute to naive_compute to check output
        # using naive approach
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())
