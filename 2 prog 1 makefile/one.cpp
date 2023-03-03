
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	cout << "enter n:";
	int n;
	cin >> n;
	/*int n = 5;*/
	double x, y, z;
	ofstream out("xyz.txt");
	for (int i = 0; i < n; i++) {
		x = (-314.0 +rand() / 314.0)/100.0;
		y = (-314.0 +rand() / 314.0)/100.0;
		z = (-314.0 +rand() / 314.0)/100.0;
		out << x << " " << y <<" "<<z<< endl;
	}
	out.close();
}