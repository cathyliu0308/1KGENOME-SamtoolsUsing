#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[])
{
	string filenames = argv[1];
	ifstream input;
	input.open(filenames.c_str());

	cout << "#!/bin/bash" << endl;
	cout << "cat ";
	string index, filename;
	while(input >> index >> filename)
	{
		cout << "data/" << filename << ".read_count ";
	}
	cout << endl;

	return 0;
}

