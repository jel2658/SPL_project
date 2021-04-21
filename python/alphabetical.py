# Program to grab a file and alphabetize its contents, creating a new .txt file
# with everything alphabetized


name = input('Enter name of file to be alphabetized:') # Input function in python prints out a statement for the user to read, then allows them to input characters, which is returned as a string.
with open(name) as f:                                  # Opening a file requires the name in the form of a string. There is the option to specify whether one is reading or writing, but
                                                       #leaving the second argument blank (ie not specifying at all) will make it default to read-only. It is considered better to put the usage of a
                                                       #file in a with statement, so it will close when the statement is finished regardless of errors.
    a = f.read()                                       # 'a' is now a copy of the file object, which can be edited in this form.
    aList = sorted(a)                                  # aList is a sorted, alphabetically and by case, list of the file.
    try:                                               # A code block intended to remove newline characters and whitespaces from the list of characters.
        while True:
            aList.remove('\n')
    except ValueError:
        pass
    try:
        while True:
            aList.remove(' ')
    except ValueError:
        pass
    aFinal = ''.join(aList)                            # aFinal is the joined string of aList, making it the alphabetical version of the file, without newlines or whitespaces.

if '.txt' in name:
    name = name.replace('.txt', '_alphabetized.txt')   # Replaces the ".txt" extension with the "_alphabetized.txt" extension to differentiate it from the old file.

with open(name, 'x') as fA:                            # I create a file to write to.
    fA.write(aFinal)                                   # Writes the alphabetized contents of the original file to the new file.

print("Alphabetization successful!")
input()						       # Waits for input in order to close.