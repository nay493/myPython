#! /usr/bin/python3

#
# example command:
#  ./zakaat1.py  --gr 3432 --gq 10 --gu tola --sr 43  --sq 500  --su grams
#
#

import argparse
import os
import sys

def minimumof(x, y):
	if x <= y:
		return x
	else:
		return y


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--gr", help="gold rate: ")
	parser.add_argument("--gq", help="gold quantity: ")
	parser.add_argument("--gu", help="gold units: ", choices = ['grams', 'tola'], nargs='?', const=1)
	parser.add_argument("--sr", help="silver rate: ")
	parser.add_argument("--sq", help="silver quantity: ")
	parser.add_argument("--su", help="silver units: ", choices = ['grams', 'tola'], nargs='?', const=1)
	args = parser.parse_args()
	
	if args.gu == 'tola':
		x = int(args.gq)
		quantity = x*10 #convert tola to gms
	else:
		quantity = int(args.gq)
	
	total_gold = quantity * int(args.gr)
	print("total_gold = {}".format(total_gold))
	total_silver = int(args.sq) * int(args.sr)
	print("total_silver = {}".format(total_silver))
	nisaab = minimumof(total_gold, total_silver)
	print("nisaab = {}".format(nisaab))
