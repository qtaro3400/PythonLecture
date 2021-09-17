# if文

age = -20
age_alcohol = 20
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license")

if not 0 < age < 120:
    print("The value is invalid!!")


# Challenge1
# ballance = 200000
# withdrawal = 150000
# if ballance > withdrawal:
#     ballance -= withdrawal
#     print("You can draw money! ballance: {}".format(ballance))
# else:
#     print("You cannnot draw money")

# Challenge2
withdrawal_limit = 1000000
ballance = 3000000
withdrawal = 1500000

if withdrawal > withdrawal_limit:
    print(f"The withdralal limit is {withdrawal_limit}")
    print("引き出し上限額を超えています")
elif ballance > withdrawal:
    ballance -= withdrawal
    print(f"You can draw money! ballance: {ballance}")
else:
    print("You cannnot draw money")