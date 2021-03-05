using System;

namespace CSharp.Baekjoon
{
    class MainApp
    {
        static void Main(string[] args)
        {
            string input = "";
            int num1, num2;
            input = Console.ReadLine();

            string[] numbers = input.Split(' ');
            num1 = Int32.Parse(numbers[0]);
            num2 = Int32.Parse(numbers[1]);
            int plus = num1 + num2;
            int minus = num1 - num2;
            int multi = num1 * num2;
            int div = num1 / num2;
            int remain = num1 % num2;
            Console.WriteLine(plus);
            Console.WriteLine(minus);
            Console.WriteLine(multi);
            Console.WriteLine(div);
            Console.WriteLine(remain);
        }
    }
}