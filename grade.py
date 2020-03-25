import sys
import argparse


class Grade(object):
    def __init__(self, points):
        self.points = points
        self.grade = ""

    def calculate(self):
        if self.points >= 91:
            self.grade = 'A'
        elif self.points >= 81:
            self.grade = 'B'
        elif self.points >= 71:
            self.grade = 'C'
        elif self.points >= 61:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def get_grade(self):
        print(self.grade)


def score_range(string):
    value = int(string)
    if value > 100 or value < 0:
        msg = "%r is not in range[0-100]" % string
        raise argparse.ArgumentTypeError(msg)
    return value


def main(argv):
    grade = Grade(argv)
    grade.calculate()
    grade.get_grade()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate grade from score')
    parser.add_argument('score', type=score_range,
                        help='score integer [0-100]')
    args = parser.parse_args()
    main(args.score)
