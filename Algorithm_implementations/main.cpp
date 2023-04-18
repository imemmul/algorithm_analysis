#include <iostream>
#include <string>
#include <fstream>
#include "TestBed.h"
#include <filesystem>


using namespace std;

int main(int argc, char* argv[]) {
	string testfile = "readme.txt";
	// if (argc < 2) {
	// 	cout << "Enter a test file name:" << endl;
	// 	cin >> testfile;
	// }
	// else {
	// 	testfile = argv[1];
	// }
	ifstream file(testfile.c_str());
	if (file.is_open()) {
		cin.rdbuf(file.rdbuf());
	}
	else {
		cout << "Error: cannot read the test file!" << endl;
		return -1;
	}
	string test_files[35] = {};
	string text;
	for(int i = 0; i < 35; i++){
		cin >> text;
		test_files[i] = text;
	} 
	for(int i = 0; i < 35; i++){
		cout << "test file is " << test_files[i] << endl;
		string test = test_files[i];
		ifstream testfile(test.c_str());
		if(testfile.is_open()){
			cin.rdbuf(testfile.rdbuf());
			int algorithmType = 0;
			int k = 0;
			// Numbers are obtained from the file line by line with cin
			cin >> algorithmType;
			cin >> k;
			// Create a TestBed object, initialize and execute the algorithm
			// ...
			TestBed *test_bed = new TestBed();
			test_bed->setAlgorithm(algorithmType, k);
			test_bed->execute();
		}
	}
	// int algorithmType = 0;
	// int k = 0;
	// // Numbers are obtained from the file line by line with cin
	// cin >> algorithmType;
	// cin >> k;
	// // Create a TestBed object, initialize and execute the algorithm
	// // ...
	// TestBed *test_bed = new TestBed();
	// test_bed->setAlgorithm(algorithmType, k);
	// test_bed->execute();
	return 0;
}
