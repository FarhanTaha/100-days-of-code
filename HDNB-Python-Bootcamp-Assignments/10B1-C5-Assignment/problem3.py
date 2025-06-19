# Problem 3: Search for a word in a text file

# Open and read the file
file = open("Search String.txt", "r")
text = file.read()
file.close()

text = text.lower()  # Convert to lowercase

# BONUS
# Search for the word user inputs despite case sensitivity
ask_user = str(input("Enter a word to search for: ")).lower()
if ask_user in text:
    print("Word exists")
else:
    print("Word does not exist")
