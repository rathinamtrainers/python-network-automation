import os

# List to hold the transactions
transactions = []

def printTransactions(t_type = "ALL"):
    for transaction in transactions:
        if t_type == "ALL" or transaction["Type"] == t_type:
            print("Date         : {}".format(transaction["Date"]))
            print("Description  : {}".format(transaction["Description"]))
            print("Type         : {}".format(transaction["Type"]))
            print("Amount       : {}".format(transaction["Amount"]))
            print("\n")


datafile = "accounts.dat"

def getValue(data):
    return data.split(":")[1].strip()

def loadData():
    # Read the data file and populate the transaction list.
    with open(datafile) as file:
        while True:
            t_date = file.readline()
            if t_date == "":
                break
            else:
                t_date = getValue(t_date)
            t_desc = getValue(file.readline())
            t_type = getValue(file.readline())
            t_amount = float(getValue(file.readline()))

            # Append the transaction to the transaction list
            transactions.append({
                "Date": t_date,
                "Description": t_desc,
                "Type": t_type,
                "Amount": t_amount})

if os.path.exists(datafile):
    loadData()
    file = open(datafile, "a")
else:
    file = open(datafile, "w")


def getTotalIncome():
    total_income = 0.0
    for transaction in transactions:
        if transaction["Type"] == "I":
            total_income += transaction["Amount"]

    return total_income


def getTotalExpenditure():
    total_expenditure = 0.0
    for transaction in transactions:
        if transaction["Type"] == "E":
            total_expenditure += transaction["Amount"]

    return total_expenditure

def getPL():
    return getTotalIncome() - getTotalExpenditure()

# function to get transaction details from app user.
def getTransactionDetails():

    # Input transaction details from user.
    t_date = input("Enter Transaction Date: ")
    t_desc = input("Enter Transaction Description: ")
    t_type = input("Enter Transaction Type (A => Asset, L => Liability, E => Expense, I => Income: ")
    t_amount = float(input("Enter Transaction Amount: "))

    # Append the transaction to the transaction list
    transactions.append({
        "Date": t_date,
        "Description": t_desc,
        "Type": t_type,
        "Amount": t_amount})

    file.write("Date: {}\n".format(t_date))
    file.write("Description: {}\n".format(t_desc))
    file.write("Type: {}\n".format(t_type))
    file.write("Amount: {}\n".format(t_amount))

def getChoice():
    print("\n\n")
    print("1. Record Transaction")
    print("2. Print Transactions")
    print("3. Print Asset Details")
    print("4. Print Liability Details")
    print("5. Print Expense Details")
    print("6. Print Income Details")
    print("7. Print Profit/Loss Statement")
    print("8. Exit")
    choice = int(input("Enter a value (1 to 8): "))
    return choice

# Main Application Loop
while True:
    choice = getChoice()

    if choice == 1:
        getTransactionDetails()
    elif choice == 2:
        printTransactions()
    elif choice == 3:
        printTransactions("A")
    elif choice == 4:
        printTransactions("L")
    elif choice == 5:
        printTransactions("E")
    elif choice == 6:
        printTransactions("I")
    elif choice == 7:
        print("Total Income: {}".format(getTotalIncome()))
        print("Total Expenditure: {}".format(getTotalExpenditure()))
        print("Profit/Loss = {}".format(getPL()))
    elif choice == 8:
        print("*** GOOD BYE ***")
        break

# Close the data file
if not file.closed:
    file.close()
