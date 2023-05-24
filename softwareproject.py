# Create the ticket class.
# The ticket class includes a layout for a list.
# The list is used to format how the data is stored and displayed.
class Ticket:
    # A counter variable is used to increment the number of tickets
    # as new tickets are created.
    counter = 1

    # __init__ is where the varaibles are initialised.
    # Initialisation creates the template for data to follow.
    # The code is executed whenever Ticket is referred to with
    # a set of values following the template.
    def __init__(self, staffID, creatorName, contactEmail, issueDesc):
        self.staffID = staffID
        self.creatorName = creatorName
        self.contactEmail = contactEmail
        self.issueDesc = issueDesc
        self.ticketNum = Ticket.counter + 2000
        Ticket.counter += 1
        self.response = "Not Yet Provided"
        self.status = "Open"

        # Checks the issueDesc field for if it contains "password change"
        # in order to run a code block which resolves the issue.
        if "password change" in self.issueDesc.lower():
            passChanged = self.staffID[:2] + self.creatorName[:3]
            self.response = "Password changed: " + passChanged
            self.status = "Closed"


# This function changes the response that has been provided with a ticket.
def ticket_response(ticketNum):
    # This counter is present in functions where
    # the user is searching for a specific ticket.
    # Its purpose is to only update if the users
    # input correctly matches a ticket present in the database,
    # and if no ticket is found, a line of code is called to
    # inform the user that no ticket matches the provided number.
    ticket_found = 0

    for ticket in ticket_list:
        if ticket.ticketNum == int(ticketNum):
            ticket_found = 1
            new_response = input("Enter ticket response: \n> ")
            ticket.response = new_response
            ticket.status = "Closed"
            show_ticket_details(ticketNum)
    if ticket_found == 0:
        print("No tickets matching provided number, returning to main menu.")

# This function displays the details of the provided ticket number.
def show_ticket_details(ticketNum):
    ticket_found = 0
    for ticket in ticket_list:
        if int(ticketNum) == ticket.ticketNum:
            ticket_found = 1
            print("Ticket Number:", ticket.ticketNum)
            print("Ticket Creator:", ticket.creatorName)
            print("Staff ID:", ticket.staffID)
            print("Email Address:", ticket.contactEmail)
            print("Issue Description:", ticket.issueDesc)
            print("Response:", ticket.response)
            print("Ticket Status:", ticket.status)
    if ticket_found == 0:
        print("No tickets matching provided number, returning to main menu.")

# This function displays how many tickets are created, resolved and open.
# Created tickets are easily checked by simply checking how many 
# objects are present in the ticket list.
# Resolved tickets are checked by running a loop that reads the status
# of each ticket present.
# Open tickets are checked by subtracting the number of resolved tickets
# from the total number of created tickets.
def get_ticket_stats():
    createdTickets = len(ticket_list)
    resolvedTickets = 0
    for t in ticket_list:
        if t.status == "Closed":
            resolvedTickets += 1
    openTickets = createdTickets - resolvedTickets
    print("Tickets Created:", createdTickets)
    print("Tickets Resolved:", resolvedTickets)
    print("Tickets Open:", openTickets)

# This function is used to create a new ticket.
# It asks the user to enter a value to be stored in a variable.
# Once the user has entered all inputs, the function calls Ticket
# to format their inputs, and then adds it to the ticket list.
# The function then displays the details of the newly created ticket.

def create_ticket():
    ticketCreator = input("Enter Ticket Creator Name: ")
    ticketID = input("Enter staffID: ")
    ticketEmail = input("Enter contact email: ")
    ticketDesc = input("Enter ticket's issue description: ")
    newTicket = Ticket(ticketCreator, ticketID, ticketEmail, ticketDesc)
    ticket_list.append(newTicket)
    show_ticket_details(newTicket.ticketNum)

# This function changes the status of the provided ticket to "Reopened".
def reopen_ticket(ticketNum):
    ticket_found = 0
    for ticket in ticket_list:
        if int(ticketNum) == ticket.ticketNum:
            ticket_found = 1
            ticket.status = "Reopened"
            show_ticket_details(ticket.ticketNum)
    if ticket_found == 0:
        print("No tickets matching provided number, returning to main menu.")

# Creates the list for tickets to be stored in.
ticket_list = []

# Example tickets
ticket1 = Ticket("MONTYB", "Montgomery Burns", "MBurns@springfield.com", "Computer disconnected from network")
ticket_list.append(ticket1)

ticket2 = Ticket("HOMERS", "Homer Simpson", "HSimpson@springfield.com", "Password Change")
ticket_list.append(ticket2)

ticket3 = Ticket("SEYMOURS", "Seymour Skinner", "SSkinner@springfield.com", "Monitor issues")
ticket_list.append(ticket3)

# The main function.
# This function contains all of the prompts that the user is
# able to see and interact with. 
# It makes use of a while loop to make sure the
# user does not accidentally end the program,
# only finishing if "Exit" is inputed.
# The function also displays the users options that they
# can input to run the other functions.
def main():
    userInput = ''
    while userInput.lower() != "exit":
        userInput = input("What would you like to do? \n Options: \n Ticket (Details), \n "
                            "(Create) Ticket, \n Ticket (Stats), \n (Reopen) Ticket, \n "
                            "(Respond) to ticket, \n (Exit) program, \n > ")
        if "details" in userInput.lower():
            userInput = input("Enter Ticket Number: ")
            show_ticket_details(userInput)

        elif "stats" in userInput.lower():
            get_ticket_stats()

        elif  "create" in userInput.lower():
            create_ticket()

        elif "reopen" in userInput.lower():
            userInput = input("Enter Ticket Number: ")
            reopen_ticket(userInput)

        elif "respond" in userInput.lower():
            userInput = input("Enter Ticket Number that you are responding to: ")
            ticket_response(userInput)

# Calling the main function so it is ran as soon as 
# Ticket is intialised, and ran after any other function
# has finished running.
main()


print("Exiting program.")
