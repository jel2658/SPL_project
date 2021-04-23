#pragma once															// File will be compiled only once.

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>														/* This collection of included items will allow the usage of the standard C++ library,
																		  file manipulation, input and output operators, strings, and vectors. C++ requires to 
																		  add such headers in one's program, otherwise the associated data objects cannot be used.*/
int main() {															/* Unlike in Python, to run a C++ program on its own, the main function must be called. This
																		contains the main statements of the program.*/

	std::cout << "Input name of file to alphabetize:" << std::endl;		/* To use the included objects, the "std::" prefix must be used. There is also the option to
																		put 'using std::[object]' before the usage of the associated data object in order to just use
																		the name of the object without 'std::', but this is considered in bad form.*/
	std::string name = "";
	std::cin >> name;													// Asks for the name of the file to be alphabetized.

	char in;
	std::vector<char> c;

	std::ifstream f;													// An input file stream object to read the necessary file.
	f.open(name);

	while (!f.eof()) {													// Continue to read the file until the end of the file.
		in = f.get();
		c.push_back(in);
	}

	f.close();															// Closes the file so that no errors occur further on.

	std::sort(c.begin(), c.end());										// The vector, which contains every character in the original file, is sorted in alphabetical order.

	std::vector<char>::iterator it = c.begin();							// To go through and manipulate the vector, I create an iterator.
	while (it != c.end()) {												// Loop that iterates through the vector of characters and erases newline characters and whitespaces.
		if ((*it) == '\n' || (*it) == ' ') {
			c.erase(it);
		}
		it++;
	}

	if (name.find(".txt") < name.length()) {							// Statement that erases '.txt' from the end of the file and adds '_alphabetized.txt' to the end.
		name.erase(name.end() - 4, name.end());
		name = name + "_alphabetized.txt";
	}
	else {
		name = name + "_alphabetized.txt";
	}

	std::ofstream a;													// A new output stream so I can write to a new file.
	a.open(name);														// Creating and opening a new file with the new name to write to.
	for (std::vector<char>::iterator it = c.begin(); it != c.end(); it++) { /* Loop that iterates through the character vector and adds the characters into the new file, now
																			in alphabetical order.*/
		a << (*it);
	}
	a.close();															// Closes the new file so that it isn't left open.

	std::cout << "File alphabetized!" << std::endl;						// Lets the user know that the program is finished.
	return 0;
}