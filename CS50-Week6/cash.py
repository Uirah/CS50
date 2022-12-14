while True:
    cents = float(input("Change: $"))
    if cents > 0:
        break

cents = round(cents*100)

count = 0

#Number of Quarters
while cents >= 25:
    cents -= 25
    count += 1

#Number of Dimes
while cents >= 10:
    cents -= 10
    count += 1

#Number of Nickels
while cents >= 5:
    cents -= 5
    count += 1

#Number of Pennys
while cents >= 1:
    cents -= 1
    count += 1

print(f"Total coins is {count}")