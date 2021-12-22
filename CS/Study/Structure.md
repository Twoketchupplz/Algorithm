# 구조체란
- 복합 데이터 형식
- 클래스와 비슷함
- 보통 필드를 `public`로 선언
    - 데이터를 담기 위한 자료 구조로 사용
    - 은닉성을 비롯한 객체 지향 원칙이 굳이 필요하지 않음

# 특징
특징 | 클래스 | 구조체
---|---|---
키워드      |`class`           |`struct`
형식        |참조 형식          |값 형식
복사        |얕은 복사          |깊은 복사
인스턴스 생성|`new`와 생성자    |선언만으로 생성
생성자 선언 |매개 변수 없이 가능|매개변수 없이 불가능
상속        |가능               |이미 직접 상속받음*

**모든 구조체는 System.Object 형식을 상속하는 System.ValueType으로부터 직접 상속받음*

- 구조체의 각 필드는 CLR이 기본값으로 초기화 해줌

# 사용
```c#
struct stName
{
    public int MyField1
    public int MyField2

    public void MyMethod()
    {
        //...
    }
}
```