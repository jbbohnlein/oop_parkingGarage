import os 
from time import sleep

class ParkingGarage():

    """
        The ParkingGarage class will have tickets, parking spaces, and current tickets.
        
        Attributes for the class: 
        - tickets: expected to be a list
        - parking spaces: expected to be a list
        - current tickets: expected to be a dictionary
    """

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets          # list
        self.parkingSpaces = parkingSpaces   # list
        self.currentTicket = currentTicket  # dictionary
        self.currentTicket = {
        'paid': False
        }

#When do the other parameters get listed with self in the methods?
#When do they get defined up in the class vs. the __init__()?

    def takeTicket(self):
# - This should decrease the amount of tickets available by 1
        if len(self.tickets) > 0:
            customers_ticket = self.tickets.pop(0)
# - This should decrease the amount of parkingSpaces available by 1 
            space_letter = self.parkingSpaces.pop(0)
            print(f'Your ticket number is {customers_ticket} and your parking space is {space_letter}. \
                \nMake sure to keep your ticket in order to exit the garage.')
        elif len(self.tickets) == 0:
            print("Sorry, the parking garage is full.")

        # tell them their ticket number


    def payForParking(self): 
    # - Display an input that waits for an amount from the user and store it in a variable
        while self.currentTicket['paid'] == False:
            ticket = int(input("Please insert your credit card and enter your ticket number: "))
            parking = input("Please enter your parking space: ")
            if ticket <=10 and ticket not in self.tickets:
            # - Update tickets list to increase by 1 (meaning add to the tickets list)
                self.tickets.append(ticket)
            # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
                self.parkingSpaces.append(parking)
            # - This should update the "currentTicket" dictionary key "paid" to True 
                self.currentTicket['paid'] = True
            # - If the payment variable is not empty (meaning the ticket has been paid) -> 
#           display a message to the user that their ticket has been paid and they have 15mins to leave
                print('Your ticket has been paid. You have 15 minutes to exit the garage.')
            else:
                print('Please try inserting your ticket number again.') 


    def leaveGarage(self):
        # - If the ticket has been paid, display a message of "Thank You, have a nice day"
        # - Once paid, display message "Thank you, have a nice day!"
        if self.currentTicket['paid'] == True:
            print('Thank you. Have a nice day!')
            self.currentTicket['paid'] = False 
             
            
east_street = ParkingGarage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], {})

def run():
    while True:
        response = input('Welcome. Do you want to take a ticket or pay for your stay? Enter: take / pay\n')
        if response.lower() == "take":
            east_street.takeTicket()
            print("Please take your ticket.")
            sleep(5)
            os.system('clear')
        elif response.lower() == "pay":
            east_street.payForParking()
            east_street.leaveGarage()
            sleep(5)
            os.system('clear')

run()