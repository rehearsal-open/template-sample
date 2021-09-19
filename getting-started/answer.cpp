#include <iostream>
#include <string>
using namespace std;

int main() {

    for (auto i = 0; i < 1000; i++) {
        int a, b;
        string ope;

        cin >> a >> ope >> b;
        switch (ope[0]) {
        case '+': cout << a + b << flush << endl; break;
        case '-': cout << a - b << flush << endl; break;
        case '*': cout << a * b << flush << endl; break;
        case '/': cout << a / b << flush << endl; break;
        case '%': cout << a % b << flush << endl; break;
        }
    }
}