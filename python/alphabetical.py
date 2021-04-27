# Program to grab a file and alphabetize its contents, creating a new .txt file
# with everything alphabetized.


name = input('Enter name of file to be alphabetized:') # Input function in python prints out a statement for the user to read, then allows them to input characters, which is returned as a string.
                                                       # Variable declaration in Python is done simply by [name of variable] = [data of variable]. This is unlike most other programming languages,
                                                       #which need a type declaration before the name of the variable or setting its data.
with open(name) as f:                                  # Opening a file requires the name in the form of a string. There is the option to specify whether one is reading or writing, but
                                                       #leaving the second argument blank (ie not specifying at all) will make it default to read-only. It is considered better to put the usage of a
                                                       #file in a with statement, so it will close when the statement is finished regardless of errors.
    a = f.read()                                       # 'a' is now a copy of the file object, which can be edited in this form.
    aList = sorted(a)                                  # aList is a sorted, alphabetically and by case, list of the file.
    try:                                               # A code block intended to remove newline characters and whitespaces from the list of characters.
        while True:                                    # 'while True:' is an infinite loop, which is not exactly "good programming practice", but in the event
                                                       #that one needs a program to continuously iterate unless an error occurs, it works. Since I use 'try:' instead of
                                                       #just having the infinite loop, if a ValueError exception is caught, then the loop terminates. This is akin to,
                                                       #perhaps, setting a while loop with a condition of throwing an error, but that isn't a possibility- at least
                                                       #in Python.
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
