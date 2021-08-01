from typing import List

import math

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.spend = 0

    def __str__(self):
        tlpad = 15 - (len(self.name))//2
        trpad = 30 - (tlpad + len(self.name))
        tl = "".ljust(tlpad, "*")
        tr = "".rjust(trpad, "*")
        top = f"{tl}{self.name.capitalize()}{tr}"
        budget = [top,"\n",]
        total = "{:.2f}".format(self.get_balance())
        for transaction in self.ledger:
            amount = "{:.2f}".format((transaction["amount"]))
            left = str(transaction["description"])
            right = str(amount)
            budget.append(left[0:23].ljust(23))
            budget.append(right[0:7].rjust(7)+"\n")
        budget.append(f"Total: {total}")
        return f'{"".join(budget)}'

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if amount < 0:
            return False
        if self.check_funds(amount) == True:
            self.spend += amount
            amount = amount * -1
            self.deposit(amount, description)
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, catagory):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {catagory.name}")
            catagory.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
            
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories: List[Category]):
    # Create title of chart.
    chart = "Percentage spent by category\n"

    # Calculate spending contributions by category.
    spend = [category.spend for category in categories]
    percentages = [math.floor(10 * spent / sum(spend)) * 10 for spent in spend]

    # Populate the histogram by row.
    for row in [[str(n).rjust(3), "| "] for n in range(100, -1, -10)]:
        chart += ''.join(row)
        chart += ''.join(
            [
                "o  " if percent >= int(row[0].strip())
                else "   " for percent in percentages
            ]
        )
        chart += '\n'
    chart += "    -" + ("---" * len(percentages)) + "\n"

    # Create a list of capitalized category names.
    names: List[str] = [category.name.capitalize() for category in categories]

    # Find the longest length.
    longest_length = max(map(len, names))

    # Create a string with each name as a vertical cascade.
    names: List[str] = [name.ljust(longest_length) for name in names]

    # Output corresponding characters side by side.
    for i in range(longest_length):
        chart += ' '*5 + "  ".join([name[i] for name in names]) + "  \n"

    return chart[:-1]