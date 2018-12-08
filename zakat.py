locals()#!/usr/bin/python3

import sys

print("Zakat\n")
print("1. Mandatory on savings exceeding 1 year\n")
print("Nisaab: Zakat mandatory exceeding how much gold ?\n")
print("Nisaab 1.: > 85 grm == 8.5 tola GOLD, then 2.5 % on all 85 grms or above\n")
print("Nisaab 2.: > 595 grm silver, then 2.5 % on all 85 grms or above\n")
print("Nisaab : which ever is lesser in the above 2 points\n")
print("Nisaab : 5% on paddy fields\n")


print("Reference: https://www.youtube.com/watch?v=XBtEbkzSoh4\n")


print('------- len(sys.argv)= ', len(sys.argv))

if len(sys.argv) < 4:
    nisaab_silver = 595*int(sys.argv[1])
    nisaab_gold = 85*int(sys.argv[2])

    print('nisaab_silver= ', nisaab_silver)
    print('nisaab_gold= ',nisaab_gold )

    if (nisaab_silver < nisaab_gold):
        nisaab = nisaab_silver
    else:
        nisaab = nisaab_gold
    print('Total saving >',nisaab, 'all savings older than 1 year must be purified(zakat)')

else:
    print("Enter sys.argv[0] <arg1> <arg2>")
    exit(0)
