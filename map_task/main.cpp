#include <iostream>
#include <map>
#include <fstream>
#include <chrono>
using namespace std;

int main()
{
    srand((unsigned)time(0));
    ofstream out("out-cpp.txt");
    int n=1;
    for (int i = 0; i < 8; i++) {
        auto t1 = chrono::high_resolution_clock::now();

        map<int, int> mmap{};
        for (int j = 0; j < n; j++) {
            mmap.insert({ j, j});
        }

        auto t2 = chrono::high_resolution_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(t2 - t1);
        cout << n << " " << int(elapsed.count()) << " " << sizeof(mmap) + 2 * n * sizeof(int) << endl;
        out << n << " " << int(elapsed.count()) <<" "<<sizeof(mmap) + 2 * n * sizeof(int) << endl;
        n *= 10;
    }
    return 0;
}
