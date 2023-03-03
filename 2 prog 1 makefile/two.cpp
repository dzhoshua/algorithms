
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
using namespace std;

int main() {
	double x, y, z;
	string line;
	ifstream in("xyz.txt");
	if (!in.is_open()) return -1;
	while(!in.eof()) {
		in>> x >> y >> z;
		cout << x << " " << y << " " << z << endl;
		double angle = 2 * sin(x)*sin(y) + cos(z);
		cout << "angle: "<< angle << endl;
	}
	in.close();
}