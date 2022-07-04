# print("Hello welcome to roll coaster game")
# number=int(input("Kindly provide your height\n"))
# if number >= 120:
#   print("You can ride the rollercoaster")
# else:
#  print("Sorry!! You need to grow taller to ride the rollercoaster")

# print("Remainder or not")
# number=int(input("Enter a number to identify\n"))
# answer=number % 2

# if answer==0:
#   print("The number providen is even")
# else:
#   print("The number provided id odd")

# print("BMI HErE I COME")
# height=float(input("Enter yoour height in m\n"))
# weight=float(input("Enter your weight in Kg\n"))
# BMI=int(weight/height**2)
# if BMI<18.5:
#   print(f"Your BMI is {BMI}, You are underweight")
# elif BMI<=25:
#   print(f"Your BMI is {BMI}, You have a normal weight")
# elif BMI<=30:
#   print(f"Your BMI is {BMI}, You are overweight")
# elif BMI<=35:
#   print(f"Your BMI is {BMI}, You are obese")
# else:
#   print(f"Your BMI is {BMI}, You clinically obese")

# print("Leap year challenge")
# Year = int(input("Enter the year to scrutinize\n"))
# if Year % 4 == 0:
#     if Year % 100 == 0:
#       print("Leap year")
#     elif Year % 400 == 0:
#         print("Leap year")
# else:
#     print("Not a leap year")


print("PIZZA CHALLENGE")
size=input("what size of pizza do you want? S,M or L\n")
bill=0
pepperoni=0
cheese=1

if size=="S":
  bill+=15
  P=bill
  pepperoni+=2
  print(f"the price is ${bill}")
elif size=="M":
  bill+=20
  P=bill
  pepperoni+=3
  print (f"The price is ${bill}")
elif size=="L":
  bill+=25
  P=bill
  pepperoni+=3
  print(f"The price is ${bill}")

else:
  print("Enter valid choice")

price=input("Do you want Pepperoni?Y or N\n")
if price=="Y":
    if pepperoni==2:
      fPrice=P+pepperoni
      print(f"The amount comes to ${fPrice}")
    elif pepperoni==3:
      fPrice=P+pepperoni
      print(f"The amount comes to ${fPrice}")
else:
  print(f"Your bill remains at {bill}")

priced=input("Do you want extra cheese? Y or N\n")
if priced=="Y":
        priceF=fPrice +cheese
        print(f"The final price is ${priceF}")
else:
  print(f"Your bill remains at {bill}")

