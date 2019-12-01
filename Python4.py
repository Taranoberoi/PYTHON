# Video 8 Codebasics hindi

# City1 = input("Enter the First City Name")
# City2 = input("Enter the Second City Name")

# n=int(n)
#
# if  n%2==0:
#     print("Even Number",n)
# else:
#     print(" Odd Number ",n)
#
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
#
# if City1 in india and City2 in india:
#     print(f'Both the cities {City1} and {City2} are in India')
# elif City1 in pakistan and City2 in pakistan:
#     print(f'Both the cities {City1} and {City2} are in pakistan')
# elif City1 in bangladesh and City2 in bangladesh:
#     print(f'Both the cities {City1} and {City2} are in bangladesh')
# else:
#     print(f' Invalid Cities or both not in the same Country ')

val = input("Enter the Fasing Sugar Level  :: ")
val=int(val)
print(type(val))

if val>=80 and val<=100:
    print(f'Sugar Value which is read{val} is low')
elif val>100:
    print(f'Sugar Value which is read{val} is high')
else:
    print("It is Normal")

