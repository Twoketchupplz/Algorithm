// https://www.acmicpc.net/problem/10952

using System;
using System.Collections.Generic;
using System.Text;

class MainApp {
    static void Main(string[] args) {
        int num1, num2;
        string[] numArr;

        while (true) {
            numArr = Console.ReadLine().Split(' ');
            num1 = int.Parse(numArr[0]);
            num2 = int.Parse(numArr[1]);

            if ((num1 == 0) && (num2 == 0)) break;

            Console.WriteLine(num1 + num2);
        }

    }
}