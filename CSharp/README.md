# C# Programming
## chapter 02 : 프로그램의 골자
### 네임스페이스
- 개체를 구분할 수 있는 범위. 하나의 네임스페이스는 하나의 개체를 가리킴
- 성격이나 하는 일이 비슷한 클래스, 구조체, 인터페이스, 델리게이트, 열거 타입 등을 하나의 이름 아래 묶음
- 네임스페이스를 사용하는 방법
    1. 네임스페이스와 클래스명을 모두 붙여줌.
        ```c#
        static void Main(string[] args)
        {
            System.Console.WriteLine();
        }
        ```
    2. `using`을 사용하여 cs파일에서 사용하고자 하는 네임스페이스를 한번 설정해 주고 이후 해당 파일 내에서 네임스페이스 없이 직접 클래스를 사용하는 방법이다.
        ```c#
        using System;

        static void Main(string[] args)
        {
            Console.WriteLine();
        }
        ```

### 클래스
데이터와 데이터를 처리하는 메소드로 이루어짐
















## [데이터 타입 구분](Study/Numeric_Types.md)
구분 1
1. 기본 데이터 타입 (Primitive Type)
    - 값 타입
        - 숫자 데이터 타입
        - 논리 타입
    - 참조 타입
        - 문자열 타입
        - 오브젝트 타입
2. 상수(Constants)
3. 열거형(Enumerator)
4. 복합 데이터 타입(Complex Data Type)

구분 2
1. 값 타입(Value Type)
    - 스택에 저장
    - 코드 블록 안에서 생성된 모든 값 타입의 변수들은 블록이 끝나면 메모리에서 제거
2. 참조 타입(Reference Type)
    - 힙에 데이터를 저장, 스택에 데이터가 저장된 힙 메모리 주소를 저장
    - 때문에 데이터 자체는 생명을 유지


```

### 문자열을 숫자로  변환할 때
Convert  
- `Boolean` `Char` `SByte` `Byte` `Int16` `Int32` `Int64` `UInt16` `UInt32` `UInt64` `Single` `Double` `Decimal` `DateTime` 및 `String` 타입으로 변환을 지원한다.
  
- 인수 타입이 맞지 않는 경우 `FormatException`을, `null`인 경우 `0`을 반환한다. 예외처리를 안하므로 독이 될 수 있다.
```c#
// 정수 타입
string textInt = "123";
int number = Convert.ToInt16(textInt) // (16: short), (32: int), (64: long)
```
Parse
- `Type.Parse(string)`형태로 쓰인다.
- 인수 타입이 올바르지 않은 경우 `FormatException`을, `null`인 경우 `ArgumentNullException`을 반환한다.
```c#
// 부동소수점 타입
string textFloat = "1.23456";
float numFloat = float.Parse(textFloat);
```

전역변수
- C#은 C/C++과 달리 가독성과 오류 방지를 위해 전역변수를 지원하지 않도록 설계했다. 하지만 이를 대체하는 필드가 있다.

## chapter 07: 클래스
클래스 안에 선언된 변수들을 일컬어 필드라고 한다.
필드를 비롯한 메소드, 프로퍼티, 이벤트 등 클래스 내에 선언되어 있는 요소들을 일컬어 멤버라고 한다.

클래스는 복합 데이터 타입이고 이는 참조타입이다.
```c#
Cat kitty;
```
위와 같은 선언문에서 `kitty`는 `null`을 가진다. `kitty`자체에 메모리가 할당되는 것이 아니라 참조로써 객체가 있는 곳을 가리킨다.
`new`연산자와 생성자를 이용해 힙에 객체를 생성하고 `kitty`가 힙에 생성된 객체를 가리킨다.
```c#
Cat kitty = new Cat();
```

## FAQ
### 숫자를 문자열로 변환할 때
```c#
int number = 123;
string text = number.ToString();