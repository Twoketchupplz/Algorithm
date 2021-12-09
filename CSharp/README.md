# C# Programming
## 네임스페이스
- 개체를 구분할 수 있는 범위. 하나의 네임스페이스는 하나의 개체를 가리킴
- 성격이나 하는 일이 비슷한 클래스, 구조체, 인터페이스, 델리게이트, 열거 형식 등을 하나의 이름 아래 묶음
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











## [데이터 형식 구분](Study/DataTypes.md)
구분 1
1. 기본 데이터 형식 (Primitive Type)
    - 값 형식
        - 숫자 데이터 형식
        - 논리 형식
    - 참조 형식
        - 문자열 형식
        - 오브젝트 형식
2. 상수(Constants)
3. 열거형(Enumerator)
4. 복합 데이터 형식(Complex Data Type)

구분 2
1. 값 형식(Value Type)
2. 참조 형식(Reference Type)

## 데이터 형식 변환
- 박싱/언박싱





## FAQ
