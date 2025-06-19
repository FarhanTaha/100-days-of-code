# Problem 2: Find the most repeated word in a text file

# Open and read the file
file = open("Repeated Lines.txt", "r")
text = file.read()
file.close()

# Removing punctuations
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")

text = text.lower() # Convert to lowercase

words = text.split() # Making a list of words

# Counting frequency of each word
wrd_count = {}

for x in words:
    if x in wrd_count:
        wrd_count[x] += 1
    else:
        wrd_count[x] = 1

# Finding the most repeated word
most_word = ""
most_count = 0

for word in wrd_count:
    if wrd_count[word] > most_count:
        most_word = word
        most_count = wrd_count[word]

# Answer
print("The most repeated word is '" + most_word + "' which appears", most_count, "times.")
