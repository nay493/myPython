import argparse
zakaat(amout, percentage)

gold(rate_of_gold, grams)
silver(rate_of_silver, grams)

zakWajib = ["gold", "silver", "plot"]
limit =	{'gold': '85 gm',
		'silver': '585 gm',
		'plot': '',
		'stock': '',
		'paddy': '20 mann'
		'treasure': '20 percent'
		'animals': '>4 5:1'
}

zakNotGivenTo = ['gairMuslim', 'tandurust', 'patienHavingMoney', 'QuarnBuy', 'kafan', 'schools', 'marriage', 'workers', 'peshawar mangnewale', 'be namaazi', 'bad aqlaakh', 'biddati', 'syed_from_nabi_khandaan', 'notForpallenewaloku', ]

#
# Reference:
# https://www.youtube.com/watch?v=7ghVzq3t-4o
#fasl yearly n times where n is no. of times fasl katthi hai
# which can be stocked for years like paddy, wheat, dates, etc zakaat should be removed
# zakaat(amount, 5) --> if water from electricity
# zakaat(amount, 10) --> if water from Nature
# 
# A land kept for years before re-sale, intended always for selling at the right price,
# is not liable to zakah until it is sold. On receipt of the price, zakah is payable on the whole amount received, once only.
# 
# There is no Zakat due on the house that a person owns and lives in or in the house that he or she owns but their dependents (wives / children etc.) live in.
# There may, however, be Zakat applicable on any other property or building that a person owns.
#
print limit['gold']
