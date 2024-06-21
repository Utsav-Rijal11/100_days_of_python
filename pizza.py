print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill=0
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size=="S":
  bill=15
  if add_pepperoni=="Y":
    if extra_cheese=="Y":
      bill=bill+2+1
    else:
      bill=bill+2
  else:
    if extra_cheese=="Y":
      bill=bill+1
    else:
      bill=bill


elif size=="M":
  bill=20
  if add_pepperoni=="Y":
    if extra_cheese=="Y":
      bill=bill+3+1
    else:
      bill=bill+3
  else:
    if extra_cheese=="Y":
      bill=bill+1
    else:
      bill=bill

else:
  bill=25
  if add_pepperoni=="Y":
    if extra_cheese=="Y":
      bill=bill+3+1
    else:
      bill=bill+3
  else:
    if extra_cheese=="Y":
      bill=bill+1
    else:
      bill=bill

print(f"Your final bill is: ${bill}.")
