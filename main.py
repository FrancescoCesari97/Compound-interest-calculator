#  python compund interest calculator


principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("principle can't be less then or equal to zero")


while rate <= 0:
    rate = float(input("Enter the interest rate amount:"))
    if rate <= 0:
        print("rate can't be less then or equal to zero")


while time <= 0:
    time = int(input("Enter the time in years:"))
    if time <= 0:
        print("principle can't be less then or equal to zero")


print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)

print(f"balance after {time} year/s: ${total:.2f}")