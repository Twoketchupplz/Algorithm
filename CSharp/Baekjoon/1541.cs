/* 1541번 잃어버린 괄호 https://www.acmicpc.net/problem/1541
 맨처음에 나오는 숫자를 제외하곤
 어떤수든 뺄셈을 해주면 된다. 괄호수가 제한이 없기 때문에 내 입맛대로 뺄셈이 가능하다.*/


using System;
using System.Collections;

public class MainApp
{
    static void Main(string[] args)
    {
        string input = Console.ReadLine();
        ArrayList expression = new ArrayList();
        ArrayList operand = new ArrayList();
        string strInteger = "";
        int ctoi;
        int ans = 0;
        bool minus = false;

        operand.Add('+');

        // 첫 뺄셈이 나온 이후로는 모든 덧셈은 뺄셈으로 바꾼다.
        foreach (char strAtom in input)
        {
            if (strAtom == '+') operand.Add(!minus ? '+' : '-');
            else if (strAtom == '-')
            {
                operand.Add('-');
                minus = true;
            }
            else
            {
                strInteger += strAtom;
                continue;
            }

            ctoi = Convert.ToInt32(strInteger);
            expression.Add(ctoi);
            strInteger = "";
        }

        ctoi = Convert.ToInt32(strInteger);
        expression.Add(ctoi);

        for (int i = 0; i < expression.Count; i++)
        {
            if ((char) operand[i] == '+') ans += (int) expression[i];
            else ans -= (int) expression[i];
        }

        Console.WriteLine(ans);
    }
}