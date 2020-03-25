import argparse

grades = {
    "A": (91, 100),
    "B": (81, 90),
    "C": (71, 80),
    "D": (61, 70),
    "F": (0, 60)
}


def score_range(string):
    value = int(string)
    if value > 100 or value < 0:
        msg = "%r is not in range[0-100]" % string
        raise argparse.ArgumentTypeError(msg)
    return value


def main(argv):
    print({k: v for k, v in grades.items()
           if v[0] <= argv and v[1] >= argv}.__iter__().__next__())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate grade from score')
    parser.add_argument('score', type=score_range,
                        help='an integer for the accumulator [0-100]')
    args = parser.parse_args()
    main(args.score)
