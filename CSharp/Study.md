# C# Programming
## chapter 03: 타입 변환
 - 값 형식의 변수는 스택에 저장된다. 코드 블록 안에서 생성된 모든 값 형식의 변수들은 블록이 끝나면 메모리에서 제거된다.
 - 참조 형식의 변수는 힙에 데이터를 저장하고 스택에는 그 데이터가 저장된 힙 메모리 주소를 저장한다. 그러므로 데이터 자체는 생명을 유지한다.

### 문자열을 숫자로 변환할 때
```c#
int number = 123;
string text = number.ToString();
```

### 숫자를 문자열로  변환할 때
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
- 인수 타입이 옳바르지 않은 경우 `FormatException`을, `null`인 경우 `ArgumentNullException`을 반환한다.
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

클래스는 복합 데이터 형식이고 이는 참조형식이다.
```c#
Cat kitty;
```
위와 같은 선언문에서 `kitty`는 `null`을 가진다. `kitty`자체에 메모리가 할당되는 것이 아니라 참조로써 객체가 있는 곳을 가리킨다.
`new`연산자와 생성자를 이용해 힙에 객체를 생성하고 `kitty`가 힙에 생성된 객체를 가리킨다.
```c#
Cat kitty = new Cat();
```
