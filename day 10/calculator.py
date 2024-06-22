#calculator
import os
from calculator_logo import logo


Task_complete=False
#add
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def product(n1,n2):
  return n1*n2

#division
def division(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":product,
  "/":division 
}


def symbol_print():
  for symbols in operations:
    print(symbols)


def calculator():
  print(logo)
  
  num1=float(input("Enter 1st number: "))
  print("What do you want to do?")
  symbol_print()
  continue_calculation=True
  
  while continue_calculation:
    operation_symbol=input("Enter a symbol form above to perform calculation: ")
    calculation_function=operations[operation_symbol]
    num2=float(input("Enter 2nd number: "))
    answer=calculation_function(num1,num2)
    print(f"{num1}{operation_symbol}{num2}={answer}")
  
    user_choice=input("Want to calculate further. Type y for yes and n for new calculation and x key to exit").lower()
    if user_choice=="y":
      num1=answer
    elif user_choice=="n":
      continue_calculation=False
      os.system("cls")
      calculator()
    elif user_choice=="x":
      continue_calculation=False
      print("Calculator is off! press run to initiate.")

calculator()     
      


  
  
  

  

    





              
              
  
   
  
