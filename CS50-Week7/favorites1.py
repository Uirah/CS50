import csv

titles = {}

with open("Favorite TV Shows - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if title not in titles:
            titles[title] = 0
        titles[title] += 1

# Can take this out and use lambda... instead of key=f
# def f(title):
# return titles[title]


for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title, titles[title])
