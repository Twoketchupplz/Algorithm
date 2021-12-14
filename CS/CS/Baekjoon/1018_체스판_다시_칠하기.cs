// https://www.acmicpc.net/problem/1018

using System;
using System.Collections.Generic;
using System.Text;

namespace Chess
{
    class MainApp
    {
        static char[,] colorBoard;
        static void Main(string[] args)
        {
            string[] inpNum = Console.ReadLine().Split(' ');
            int M = int.Parse(inpNum[0]);
            int N = int.Parse(inpNum[1]);
            colorBoard = new char[M, N];


        }

    }
}
