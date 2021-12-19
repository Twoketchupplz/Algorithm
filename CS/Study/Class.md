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