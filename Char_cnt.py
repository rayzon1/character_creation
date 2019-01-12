"""
This program will scan a text file and print out only the number of vowels in
the text
"""

# allows the user to input a file.txt and count the number of char it appears
def count_char(text, char):
    count = 0
    for x in text:
        if x == char:
            count += 1
    return count

file = open("new_text.txt", "w")
file.write("""fuck your mother, motherfucker fuck your mother, motherfucker
	fuck your mother, motherfuckerfuck your mother, motherfuckerfuck your mother, motherfucker
	fuck your mother, motherfuckerfuck your mother, motherfucker""")

file.close()

# will prompt the user to input a filename and open the .txt file as the variable
# x

filename = "new_text.txt"
with open(filename) as f:
	text = f.read()

for char in 'aeiou':
	perc = 100 * count_char(text, char) / len(text)
	print("{0} - {1}%".format(char,round(perc,2)))
