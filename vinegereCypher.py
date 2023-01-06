
# Create the Vigenere table.
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Get input from the user (plaintext and key).
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

# Convert plaintext and key to all upper case letters.
plaintext = plaintext.upper()
key = key.upper()

# Remove all non-letters from plaintext and key.
def remove_non_letters(original):
    """This function takes in a string and returns a string with
all non-letter characters removed. Used for removing non-letter
characters from plaintext and key."""
    new = ''
    for i in range(len(original)):
        letter = original[i].isalpha()
        if letter:
            new += original[i]
    return new

key = remove_non_letters(key)
plaintext = remove_non_letters(plaintext)

# Encrypt plaintext.

encrypt = '' #Encryption string.
count = 0 #Track current letter of key.
index = -1  #Index of encrypted letter in table.

for i in range(len(plaintext)):
    #Add index of plaintext letter in table and index of key letter in table.
    index = table.index(plaintext[i]) + table.index(key[count])
    
    if index < 0:
        print("error.") 
    elif index >= 26: 
        index -= 26
    encrypt += table[index]
    
    #Set counting of key.
    count += 1
    if count >= len(key):
        count = 0
        
# Show result on screen.
print("Encryption: " + encrypt)

