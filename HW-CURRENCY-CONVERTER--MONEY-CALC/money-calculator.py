# Money Calc

# INS
# * amount of money $
# * bills (1,5)
# OUT:
# * numbers of bills
# 7 -> 1 x $5 + 2 x $1 
# 10 -> 2 x $5 + 0 x $1
# 11 -> 2x $5 + 1 x $1

# HW1:  what if bills (1,5,20)

money    = int( input( "Enter $:" ) )


# HW1:  what if bills (1,5,20)
bills_20 = money // 20

bills_5  = (money - bills_20 * 20) // 5 

bills_1  = money % 5


print( bills_20, "x $20 +", bills_5, "x $5 +", bills_1, "x $1")