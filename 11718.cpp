#include<iostream>
#include<string>

using namespace std;

int main() {
    string str;
    int i = 0;
    while (true) {
        getline(cin, str);
        if (str == "")
            break;
        cout << str << endl;
    }
    return 0;
}

/*
 * 검색자료 https://aorica.tistory.com/10
 */