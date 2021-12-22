# 1. 멤버
## 1.1. 필드
- 클래스 안에 선언된 변수
- 필드는 프로그램에서 유일하게 존재
    - 왜 why?
    - 한 프로그램에 임의의 클래스는 유일(인스턴스가 여러개)
    - 필드는 클래스에 소속

## 1.2. 메소드
### 생성자
- 클래스 선언 시 구현하지 않아도 컴파일러에서 만듦
- 오버로딩으로 다양한 생성자 구현 가능
    
```c#
Cat kitty;
// kitty자체에 메모리가 할당되는 것이 아니라 참조로써 객체가 있는 곳을 가리킨다.
// 쓰레기값
```

```c#
Cat kitty = new Cat();
// `new`연산자와 생성자를 이용해 힙에 객체를 생성
// `kitty`가 힙에 생성된 객체를 가리킴
```


### 소멸자
- `~ClassName(){}`
- 오버로딩, 직접 호출 불가
- 가비지 컬렉터(GC)가 판단하여 호출
- 가급적 사용하지 않는다
    - GC가 대부분 정확하게 움직임
    - GC 동작 예측이 어려움
    - 구현된 소멸자는 GC가 클래스의 족보를 타고 올라가며 호출하여 성능 저하 유발






---
---
# 2. `Static` 키워드
- 클래스 자체에 소속됨
- 인스턴스 생성 없이 호출 가능


### 정적 메소드(Static Method)
- 프로그램 전체에 걸쳐 공유해야 하는 경우
- 객체 내부의 데이터를 이용할 일이 없는 경우


### 인스턴스 메소드(Instance Method)
- 인스턴스에 소속됨
- 인스턴스를 생성해야 호출 가능
- 객체 내부의 데이터를 이용해야 하는 경우






---
---
# 3. `this` 키워드
- 객체 내부에서 자신의 필드나 메소드에 접근하는 방법
```c#
class MyClass{
    int a, b, c;

    public MyClass(){
        this.a = 1;
    }

    public MyClass(int b) : this(){ // MyClass()를 호출 
        this.b = b;
    }

    public MyClass(int b, int c) : this(b){ // MyClass(int)를 호출
        this.c = c;
    }
}
```





---
---
# 4. 복사
```c#
MyClass src = new MyClass();
MyClass trg = src;
```
- `trg`의 필드값이 변경되면 `src`도 같이 변경됨
    - 왜 why? 참조형식
        - 힙에 저장된 필드값의 주소를 스택에 변수명이 가리키고 있음
        - 주소를 복사했으므로 같은 주소지 필드값에 접근하게 됨

```c#
class MyClass{
    public int MyField;

    public MyClass DeepCopy(){
        MyClass newCopy = new MyClass();

        // 그러므로 멤버를 직접 복사해야 함
        newCopy.MyField = this.MyField;

        return newCopy;
    }
}
```




---
---
# 5. 접근 한정자(Access Modifier)
- OOP의 은닉성
    - 필요한 최소 기능만 노출하고 내부를 감출 것
    - 필드는 상수를 제외하고는 꼭 감추는 것이 좋다
- 필드, 메소드, 프로퍼티 등 모든 요소에 대해 사용 가능

접근 한정자 | 설명
--- | ---
`public` |            클래스 내부/외부 모든 곳에서 접근 가능
`protected` |         파생 클래스에서 접근 가능
`private` |           클래스 내부에서 접근 가능, 파생 클래스도 접근 불가
`internal` |          같은 어셈블리에 있는 코드에서 `public`으로 접근 가능, 다른 어셈블리에 있는 코드에서는 `private`
`protected internal` |같은 어셈블리에 있는 코드에서 `protected`로 접근 가능, 다른 어셈블리에 있는 코드에서는 `private`

- 수식하지 않은 클래스 멤버는 `private`로 자동 지정





---
---
# 6. 상속
- 파생 클래스는 객체 생성시 기반 클래스의 생성자 호출 후 자신의 생성자를 호출
- 소멸 시 반대 순서로 소멸자를 호출

## 6.1. `base` 키워드
- 기반 클래스에 접근하는 키워드
- 기반 클래스 생성자에게 매개 변수 전달
```c#
class ParentClass
{
    protected string Name;
    public ParentClass(string name) // 생성자
    {
        this.Name = name;
    }
}

class ChildClass
{
    public ChildClass(string name) : base(name) // base 키워드로 전달
    {
        // code, code and code..
    }
}
```

## 6.2. ``sealed` 한정자
- 상속 봉인
    - 의도하지 않은 상속이나 파생 클래스의 구현을 방지
    - 상속 시 컴파일러가 에러 메시지 출력
```c#
sealed class ParentClass
{
    // ...
}
```






---
---
# 7. 형식 변환
## 7.1. 활용
- 기반 클래스와 파생 클래스 간 형식 변환이 가능
- 파생 클래스의 인스턴스는 기반 클래스의 인스턴스로 사용 가능
```c#
Parent parent = new Parent();
parent = new Child(); // 파생 클래스 참조, 기반 클래스의 인스턴스로 사용
Child child = (Child)parent; // 형 변환
```
- 다른 클래스에서 자식마다 메소드를 오버로딩하여 구현하기 보단, 부모 클래스 형식을 매개변수로 구현하면 편리함
```c#
class OtherClass 
{
    public void SomeMethod(Parent parentParam) // 자식 클래스를 인자로
    {
        /*...*/
    }
}
```



## 7.2. 형변환 연산자
연산자|설명
---|---
is   | 객체가 해당 형식에 해당하는지 검사하여 결과를 `bool` 값으로 반환
as   | 형식 변환 연산자와 같은 역할<br> 변환에 실패시 예외를 일으키지 않고(형변환 연산자와 다르게, 그래서 권장됨),<br> 객체 참조를 `null`로 만듦








---
---
# 8. 오버라이딩
*Override 우선하다. 부모 클래스의 메소드보다 우선되어 메소드 호출시 오버라이딩된 메소드가 호출됨*

## 8.1. 다형성(Polymorphism)
- 객체가 여러 형태를 가질 수 있음
- 파생 클래스를 통해 다형성을 실현

## 8.2. 오버라이딩 하기
### `virtual`, `override` 키워드
- 오버라이딩할 메소드는 `virtual` 키워드로 한정
- 재정의하는 메소드는 `override` 키워드로 한정
- `private`로 선언한 메소드는 파생 클래스에서 보이지도 않고, 오버라이딩도 불가

## 8.3. 메소드 숨기기
```c#
class Derived : Base
{
    public new void MyMethod() // new 한정자로 메소드 숨기기
    {
        // code..
    }
}
```
- `new` 한정자 사용 (연산자 `new`와 다른 동명이키)
- 상속받은 기반 클래스 메소드를 숨기고 파생 클래스에서 새로 구현
- 오버라이딩과 차이점
    - 부모 클래스 형식의 객체를 선언하고 메소드를 호출하면 기반 클래스 메소드가 다시 드러남

## 8.4. 오버라이딩 봉인
- 해당 메소드 앞에 `sealed` 키워드 사용
- 파생의 파생클래스에서 오버라이딩을 원치 않은 경우 유용
    - 오버라이딩한 메소드는 자동으로 오버라이딩 가능










---
---
# 9. 중첩 클래스
- 클래스 안에 선언된 클래스
- 자신이 소속된 클래스의 멤버(`private` 멤버까지)에 자유롭게 접근
- 왜 사용하나요?
    - 클래스 외부에 공개하고 싶지 않은 형식
    - 현재의클래스의 일부분처럼 표현할 수 있는 클래스를 만들고 싶을 때
        - 현실 표현
- 은닉성을 무너뜨리지만(`private` 멤버 침해) 유연한 프로그래밍 가능





---
---
# 10. 분할 클래스
- 여러번 나눠 구현하는 클래스
- 클래스 구현이 길어질 경우 여러 파일에 나눠서 구현하는 기능
- 클래스 구현 앞에 `partial` 키워드 사용







---
---
# 11. 확장 메소드
- 기존 클래스의 기능 확장
    - 상속이 아님
- 선언 방법
    1. `static` 한정자로 수식한 새로운 클래스 선언
    2. `static` 한정자로 수식한 확장 메소드 선언
    3. 첫 번째 매개 변수는 `this` 키워드와 함께 확장하고자 하는 클래스(또는 형식)의 인스턴스
```c#
// 선언
namespace MyExtension
{
    public static class IntegerExtension
    {
        public static int Power(this int myInt, int exp)
        {
            // power code..
        }
    }
}

// 사용
using MyExtension; //네임스페이스 사용
int a = 2;
int b = a.Power( 3 ); // Power()가 원래 int 형식의 메소드였던 것처럼 사용 가능
```
