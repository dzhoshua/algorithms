#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
using namespace std;
//g++ -std=c++17 .\main.cpp

int sum = 0;

string func(string path) {
	for (const auto& entry : std::filesystem::directory_iterator(path)) {
		cout << entry.path() << endl;
		if (entry.is_regular_file()) {
			ifstream in(entry.path().string());
			if (!in.is_open()) return "error";
			int num;
			while (!in.eof()) {
				in >> num;
				sum += num;
			}
			in.close();
		}
		if (entry.is_directory()) {
			func(entry.path().string());
			cout << entry.path() / "out" << endl;
		}
	}
	return path;
}

int main(void) {
	string path = "data";
	func(path);
	cout << "SUM = "<<sum<<endl;
	cout << "END";
	return 0;
}
