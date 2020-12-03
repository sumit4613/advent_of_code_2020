import argparse
import collections


def naive_compute(s: str) -> int:
    """Using string.count method"""
    count = 0
    for line in s.splitlines():
        limit, code, password = line.split()
        l_limit, r_limit = limit.split("-")
        left_limit, right_limit = int(l_limit), int(r_limit)
        code = code[0]

        counts = password.count(code)
        if left_limit <= counts <= right_limit:
            count += 1

    return count


def compute(s: str) -> int:
    counter = 0
    for line in s.splitlines():
        limit, code, password = line.split()
        l_limit, r_limit = limit.split("-")
        left_limit, right_limit = int(l_limit), int(r_limit)
        code = code[0]

        counts = collections.Counter(password)[code]
        if left_limit <= counts <= right_limit:
            counter += 1

    return counter


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
