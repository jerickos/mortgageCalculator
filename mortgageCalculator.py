
import datetime as dt
from dateutils import month_start, relativedelta
import matplotlib.pyplot as plt
import numpy_financial as npf
import pandas as pd

class Loan:

    def __init__(self, rate, term, loan_amount, start=dt.date.today().isoformat()):
        self.rate = rate / 1200
        self.periods = term * 12
        self.loan_amount = loan_amount
        self.start = month_start(dt.date.fromisoformat(start) + dt.timedelta(31))
        self.pmt = npf.pmt(self.rate, self.periods, -self.loan_amount)
        self.pmt_str = f"${self.pmt:,.2f}"
        self.table = self.loan_table()

    def loan_table(self):
        periods = [self.start + relativedelta(months=x) for x in range(self.periods)]
        interest = [npf.ipmt(self.rate, month, self.periods, -self.loan_amount)
                    for month in range(1, self.periods + 1)]
        principal = [npf.ppmt(self.rate, month, self.periods, -self.loan_amount)
                     for month in range(1, self.periods + 1)]
        table = pd.DataFrame({'Payment': self.pmt,
                              'Interest': interest,
                              'Principal': principal}, index=pd.to_datetime(periods))
        table['Balance'] = self.loan_amount - table['Principal'].cumsum()
        return table.round(2)

    def plot_balances(self):
        amort = self.loan_table()
        plt.plot(amort.Balance, label='Balance')
        plt.plot(amort.Interest.cumsum(), label='Interest Paid')
        plt.grid(axis='y', alpha=.5)
        plt.legend(loc=8)
        plt.show()

    def summary(self):
        amort = self.table
        print("Summary")
        print("-" * 30)
        print(f'Payment: {self.pmt_str:>21}')
        print(f'{"Payoff Date:":19s} {amort.index.date[-1]}')
        print(f'Interest Paid: {amort.Interest.cumsum()[-1]:>15,.2f}')
        print("-" * 30)

    def pay_early(self, extra_amt):
        return f'{round(npf.nper(self.rate, self.pmt + extra_amt, -self.loan_amount) / 12, 2)}'

    def retire_debt(self, years_to_debt_free):
        extra_pmt = 1
        while npf.nper(self.rate, self.pmt + extra_pmt, -self.loan_amount) / 12 > years_to_debt_free:
            extra_pmt += 1
        return extra_pmt, self.pmt + extra_pmt





customerName = input("Hello welcom to Mortage Calculator. Lets get started by what is your name? ")
customerLoadAmount = input("Hello, " + str(customerName) + "! What is your load amount for your property?")
customerLoadAmount = float(customerLoadAmount)
customerInterest = input("Please provide your intenest rate. ")
customerInterest = float(customerInterest)

print("Based on the information you provided, we have calculated your monthly payment, for a 15 year term and a 30 year term")
option1 = Loan(customerInterest, 15, customerLoadAmount)
print("A 15 year term has a monthly payment of ", option1.pmt)
option2 = Loan(customerInterest, 30, customerLoadAmount)
print("A 30 year term has a monthly payment of ", option2.pmt)
term_c = input("Which term do you perfer?")
term_c = int(term_c)


customer_Loan = Loan(customerInterest, term_c, customerLoadAmount)
print(customer_Loan.summary())
print(customerName, ", thank you for choosing Morgage Calculator for your finicial help.")




"""


example = Loan(3.5, 15, 500000)
print(example.summary())

loadQuestion = input("Have you decide a load term? ")
loadQuestion = loadQuestion.lower()


example = Loan(3.5, 15, 500000)
print(example.summary())


if loadQuestion == "no":
    print("Mortgage Calculator has listed a 15 year lease and a 30 year lease")
    term15 = Loan(customerInterest, customerLoadAmount, 15)
    print(term15.pmt)
    term30 = Loan(customerInterest, customerLoadAmount, 30)
    print(term30.pmt)

customerTerm = input("Please enter your loan term.")
customerTerm = float(customerTerm)

customer_Loan = Loan(customerInterest, customerTerm, customerLoadAmount)
print(customer_Loan.summary())


class Loan:

    def __init__(self, rate, term, loan_amount, start = dt.date.today().isoformat()):
        self.rate = rate / 1200
        self.periods = term * 12
        self.loan_amount = loan_amount
        self.start = month_start(dt.date.fromisoformat(start)) + dt.timedelta(31)
        self.pmt = npf.pmt(self.rate, self.periods, -self.loan_amount)
        self.pmt_str = f"${self.pmt:,.2f}"
        self.table = self.loan_table()
    
    def loan_table(self):
        periods = [self.start + relativedelta(month=x) for x in range(self.periods)]
        interest = [npf.ipmt(self.rate, month, self.periods, -self.loan_amount)
                    for month in range(1, self.periods + 1)]
        principal = [npf.ppmt(self.rate, month, self.periods, -self.loan_amount)
                    for month in range(1, self.periods + 1)]
        table = pd.DataFrame({'Payment' : self.pmt, 'Interest' : interest, 'Principal' : principal}, index=pd.to_datetime(periods))

        table['Balance'] = self.loan_amount - table['Principal'].cumsum()
        return table.round(2)

loan = Loan(5.875, 30, 360000)
print(loan.table)



customerName = input("Hello welcom to Mortage Calculator. What is your name? ")
customerLoadAmount = input("Hello, " + str(customerName) + "! What is your load amount for your property?")
customerLoadAmount = float(customerLoadAmount)
customerInterest = input("Please provide your intenest rate. ")
customerInterest = float(customerInterest)
loadQuestion = input("Have you decide a load term? ")

if loadQuestion == "no":
    print("Mortgage Calculator has listed a 15 year lease and a 30 year lease")
    term15 = Loan(customerLoadAmount, customerInterest, 15)
    term15.monthlyPayment()
    term30 = Loan(customerLoadAmount, customerInterest, 30)
    term30.monthlyPayment()
elif loadQuestion == "yes":
    loanterm = input("Please provide your loan term?")

else:
    print("error")

customersTerm = input("Whcih term do you perfer, a 15 year or a 30 year term? ")
def monthlyPayment(self):
        interestCalculation = self.interest / 100 / 12
        termCalculation = self.term * 12
        payment = (interestCalculation * self.loanAmount) / (1 - (1 + interestCalculation) ** -termCalculation)
        return print("$ " + str(payment))

loan = Loan(5.875, 30, 360000)
print(loan.table)
"""