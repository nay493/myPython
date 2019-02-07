import argparse


parser = argparse.ArgumentParser(description='calculate volume')
parser.add_argument('-l', '--l', type=int , help='Enter l')
parser.add_argument('-b', '--b', type=int, help='Enter b')
parser.add_argument('-H', '--h', type=int, help='Enter h')
args = parser.parse_args()


def volume(l, b, h):
    v = l*b*h
    return v


print (volume(args.l, args.b, args.h))