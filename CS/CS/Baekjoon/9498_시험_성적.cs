// https://www.acmicpc.net/problem/9498

using System;

namespace CS.Baekjoon
{
    class MainApp
    {
        static void Main(string[] args)
        {
            string score = Console.ReadLine();
            int number = Convert.ToInt32(score);
            char grade;
            if (number >= 90) grade = 'A';
            else if (number >= 80) grade = 'B';
            else if (number >= 70) grade = 'C';
            else if (number >= 60) grade = 'D';
            else grade = 'F';

            Console.WriteLine(grade);
        }
    }
}
