This is the C++ version of the alphabetizing program that I created in Python first. The most obvious between the two is that C++ requires a main function
and inclusion statements. Python can have main functions, but running one on its own runs everything, whereas attempting to run a C++ file with no main
will simply not run the file. This does not include header files, which are simply compiled with the main C++ file when it is run. There are some exceptions,
but I am not familiar enough with them to comment. I used Visual Studio to develop this code, which has its own compiler, and compiles the code for me. The 
inclusion statements are what allow the developer to use the various components of C++. Python has something similar in its import of modules, but basic
Python had enough in it in order to code the entire program without importing anything. With C++, multiple inclusion statements were required. While C++
is an object-oriented program, most of the code written is less of that and more imperative programming- however, the manipulation of vectors and files
still shows its object-oriented side.

To use this program, simply put a .txt file in with the main.cpp file (there exist 2 there already) and run the code. Type in the full name of the file to alphabetize, including the extension, and press enter. A new file should be created in the same area, with '_alphabetized.txt' added to the end of the name.
