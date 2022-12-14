# Does not have the same result as the course site suggests, but close
text = input("Text: ")

letters = 0
words = 0
sentences = 0

for i in text:
    if i.isalpha():
        letters += 1
    elif i == " ":
        words += 1
    elif i == "." or i == "!" or i == "?":
        sentences += 1

# Coleman-Liau Index
index = 0.0588 * (letters/words*100) - 0.296 * (sentences/words*100) -15.8

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}", round(index))