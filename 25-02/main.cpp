#include <iostream>
#include <filesystem>
#include <string>
using namespace std;
//g++ -std=c++17 .\main.cpp

string func(string path) {
	for (const auto& entry : std::filesystem::directory_iterator(path)) {
		cout << entry.path() << endl;
		cout << entry.is_regular_file() << endl;
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
	return 0;
}
