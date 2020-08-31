#include <iostream>

using namespace std;

int main() {
    int A, B;
    cin >> A;
    cin >> B;
    cout.precision(10);
    cout << double(A)/B;
}

/*문제의 포인트 "절대/상대 dhcksms 10^-9까지 허용한다.
 * precision(9)를 하면 오류가 생긴다. 이유는 잘 모르나 그 이상의 오차가 발생하는듯 하다. 반올림이라던가..
 * fixed를 사용하지 않으면 precision의 범위가 소수점 아래뿐만 아니라 앞의 정수부도 포함된다. 큰수의 나눗셈을 해보자..
 * 그럼 문제의 조건이 이미 0 < A, B < 10이므로 그럴 일이 없다고 할텐데.. 의미상 fixed를 사용하는게 맞지만
 * precision(10)을 하면 여유있게 해결되는 것이다.
 */