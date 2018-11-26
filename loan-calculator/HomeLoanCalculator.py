
#Function 4: Home Loan Affordability Calculator
#Build a function maximum_home_loan(PMT, i, n) that calculates the maximum home loan that your customer can afford, if they:
#can afford to pay an amount, PMT at the END of every YEAR (with the first payment made exactly one year from now),
#at an interest rate of i% per year, compounded annually, and pay off the home over a term of n years.

#http://financeformulas.net/Loan_Payment_Formula.html

# def compound_balance(balanceamount, rate)
#     compoundinterest=balance * ((1 + rate/100)**)
#     return compoundbalance

def maximum_home_loan(PMT, i, n):
    yearlypayment=PMT
    rate=i
    maxhomeloan=(yearlypayment * (1 - ((1+rate)**-n))) / rate
    # maxhomeloan=0
    # for x in range(2,n-1):
    #     compound_balance=compound_balance()
    return maxhomeloan


print(maximum_home_loan(15000*12, 0.1045, 30))
