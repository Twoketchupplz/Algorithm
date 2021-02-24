# C# Programming
## 타입 변환
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


