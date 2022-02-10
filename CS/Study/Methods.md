# 차례
[1. 매개변수](#1-매개변수)
- [1.1. 참조에 의한 매개 변수 전달](#11-참조에-의한-매개-변수-전달)
- [1.2. 출력 전용 매개 변수](#12-출력-전용-매개-변수)
- [1.3. 가변길이 매개 변수](#13-가변길이-매개-변수)
- [1.4. 명명된 매개 변수(Named Parameter)](#14-명명된-매개-변수)
- [1.5. 선택적 매개 변수(Optional Parameter)](#15-선택적-매개-변수)

[2. 메소드 오버로딩(Overloading)](#2-메소드-오버로딩)

# 정보
- 메소드는 클래스 안에 있음을 인지할 것






# 1. 매개변수
- 매개 변수는 인수(argument)를 복사(Call by value)한 것






## 1.1. 참조에 의한 매개 변수 전달
- `ref` 키워드 사용

    ```c#
    // 선언
    static void Swap(ref int a, ref int b) {
        int temp = b;
        b = a;
        a = temp;
    }

    // 호출
    int x = 1;
    int y = 2;
    Swap(ref x, ref y);
    ```






## 1.2. 출력 전용 매개 변수
- 해당 매개 변수에 결과를 저장하지 않으면 컴파일러가 에러 메시지 출력
- `out` 키워드 사용

    ```c#
    // 선언
    void Divide(int a, int b, out int quotient, out int remainder){
        quotient = a / b;
        remainder = a % b;
    }

    // 호출
    int a = 10;
    int b = 3;
    int c;
    int d;
    Divide(a, b, out c, out d);
    ```






## 1.3. 가변길이 매개 변수
- 개수가 유연하게 변할 수 있는 매개 변수
    - 형식은 같으나 개수만 달라질 수 있는 경우
- `params`, 배열 사용
```c#
// 매개변수 numbers 배열에 argument가 모두 담긴다.
int Sum(params int[] numbers){
    int sum = 0;
    for(int i = 0; i < numbers.Length; i++){
        sum += numbers[i];
    }

    return sum;
    // 사용
    // total = Sum(1, 2, 3, 4, 5);
}
```





## 1.4. 명명된 매개 변수
- 매개 변수의 이름에 근거하여 데이터를 할당하는 기능
- 순서를 바꿀 수 있음
```c#
static void Print(string name, string phone){
    // code..
}

static void Main(string[] args){
    print(name: "Ketchup", phone : "123456");
}
```






## 1.5. 선택적 매개 변수
- 디폴트 값이 있는 매개 변수
- 데이터 할당 생략 가능
- 반드시 필수 매개 변수 뒤에 와야함
- 매개 변수가 다른데 논리는 같은 경우
```c#
void Mymethod(int a, int b = 0){
    //code..
}
```










# 2. 메소드 오버로딩
- 하나의 메소드 이름에 여러 개의 구현을 올리는 것
- 성능에 지장 없음
- 매개 변수에 따라 논리도 달라지는 경우 사용
```c#
// 예시
int Plus(int a, int b){
    //code..
}
// overloading
double Plus(double a, double b){
    //code..
}
```
*"메소드 오버로딩과 선택적 매개 변수는 동시에 사용하지 않도록 한다"*
