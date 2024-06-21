#clear garna aaudaina malai
import os


#from replit import clear
#HINT: You can call clear() to clear the output in the console.

#PRINTING LOGO

from art1 import logo
print(logo)
bidding_over=False
bids={}

def highest_bidder(bidding_record):
  hightest=0
  winner=""
  amount=0
  for bidder in bidding_record:
    bidding_amount=bidding_record[bidder]
    if bidding_amount>hightest:
      winner=bidder
      amount=bidding_amount
  print(f"The winner is:{winner} with bid amount of {amount}")
    

while not bidding_over:

  name=input("Enter your name:")
  price=int(input("Enter your bid:"))
  bids[name]=price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue=="y":
    os.system("cls")
    print(logo)
  elif should_continue=="n":
    bidding_over=True
    highest_bidder(bids)
  else:
    print("Invalid Choice")

