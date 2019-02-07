import argparse


parser = argparse.ArgumentParser()
parser.add_argument('l', type=int , help='Enter l')
parser.add_argument('b', type=int, help='Enter b')
parser.add_argument('h', type=int, help='Enter h')
args = parser.parse_args()


def volume(l, b, h):
    return l*b*h


print volume(args.l, args.b, args.h)
