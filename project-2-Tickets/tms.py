# Project: Ticket Management System.
# Write a python to manage the customer tickets. There must be an option to enter tickets for the customers.
# There must be another option to access the existing tickets and change the ticket status.
# It must be possible to query the tickets based on ticket state.
# The ticket data must be persisted in a data file.

import os

def getTicketInfo():
    global ticketID
    ticketID += 1
    name = input("Enter Customer Name: ")
    issue = input("Enter the issue: ")
    phone = input("Enter phone number: ")
    ticket = { "ID" : ticketID, "Name" : name, "Issue" : issue, "Phone" : phone, "State" : "Open"}
    tickets.append(ticket)
    persist(datafile, ticket)
    printTicketInfo(ticket)

def printTicketInfo(ticket):
    print("\n")
    print("Ticket ID     : {}".format(ticket["ID"]))
    print("Customer Name : {}".format(ticket["Name"]))
    print("Phone Number  : {}".format(ticket["Phone"]))
    print("Issue         : {}".format(ticket["Issue"]))
    print("Ticket Status : {}".format(ticket["State"]))
    print("\n")

def persist(file, ticket):
    if not file.closed:
        file.write(str(ticket) + "\n")
        file.flush()

def loadTickets():
    global ticketID
    datafile.seek(0)
    while True:
        data = datafile.readline()
        if data == "":
            break
        ticket = eval(data)
        tickets.append((ticket))
        ticketID = ticket["ID"]

def printTicketsByStatus(status = "ALL"):
    for ticket in tickets:
        if ticket["State"] == status or status == "ALL":
            printTicketInfo(ticket)

def ChangeTicketStatusInFile():
    newdatafile = open("newtms.dat", "w")
    for ticket in tickets:
        persist(newdatafile, ticket)
    newdatafile.close()

    global datafile
    datafile.close()

    os.remove(datafilename)
    os.rename("newtms.dat", datafilename)
    datafile = open(datafilename, "a+")


def changeTicketStatus():
    ticketID = int(input("Enter Ticket ID: "))

    for ticket in tickets:
        if ticket["ID"] == ticketID:
            printTicketInfo(ticket)
            newState = input("Enter new State (Open/Closed): ")
            ticket["State"] = newState
            ChangeTicketStatusInFile()
            break
    else:
        print("Ticket ID {} not found\n".format(ticketID))

def printTicketByID():
    ticketID = int(input("Enter Ticket ID: "))

    for ticket in tickets:
        if ticket["ID"] == ticketID:
            printTicketInfo(ticket)
            break
    else:
        print("Ticket ID {} not found\n".format(ticketID))

# Main program starts here (Global Scope)
datafilename = "tms.dat"
datafile = open(datafilename, "a+")
tickets = []
ticketID = 0
loadTickets()

while True:
    print("1. Create a new Ticket")
    print("2. Change Ticket Status")
    print("3. Print Open Tickets")
    print("4. Print Closed Tickets")
    print("5. Print ALL Tickets")
    print("6. Print specific Ticket")
    print("7. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        getTicketInfo()
    elif choice == 2:
        changeTicketStatus()
    elif choice == 3:
        printTicketsByStatus("Open")
    elif choice == 4:
        printTicketsByStatus("Closed")
    elif choice == 5:
        printTicketsByStatus()
    elif choice == 6:
        printTicketByID()
    elif choice == 7:
        print("*** GOOD BYE ***")
        break

if not datafile.closed:
    datafile.close()
