#include <iostream>

using namespace std;

int main() {
    int N, i;
    cin >> N;
    for (i = 0; i < N; i++) {
        cout << "Hello World, Judge " << i + 1 << "!";
        if (i < N - 1) cout << endl;
    }
}