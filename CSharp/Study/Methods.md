# 정보
- 메소드는 클래스 안에 있음을 인지할 것

# 매개변수
- 매개 변수는 인수(argument)를 복사(Call by value)한 것

## 1. 참조에 의한 매개 변수 전달
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
    Swap(ref x, ref y)
    ```


## 2. 출력 전용 매개 변수
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

    # 메소드 오버로딩(Overloading)
    - 하나의 메소드 이름에 여러 개의 구현을 올리는 것
    - 성능에 지장 없음