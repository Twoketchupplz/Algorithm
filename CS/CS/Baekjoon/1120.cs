/*
 * 1120번 문자열 https://www.acmicpc.net/problem/1120
 */

using System;

class MainApp
{
    static int _minAns;
    
    static void Main(string[] args)
    {
        string input = Console.ReadLine();
        string[] inp_split = input.Split(' ');
        
        char[] textA = new char[inp_split[0].Length];
        char[] textB = new char[inp_split[1].Length];

        _minAns = textA.Length;
        
        for (int i = 0; i < inp_split[0].Length; i++) textA[i] = inp_split[0][i];
        for (int i = 0; i < inp_split[1].Length; i++) textB[i] = inp_split[1][i];
        
        //두 문자열 이동하며 전부 비교
        for (int i = 0; i < textB.Length - textA.Length + 1; i++)
        {
            int tmp = textA.Length;
            for (int j = 0; j < textA.Length; j++)
            {
                if (textA[j] == textB[i + j]) tmp -= 1;
            }

            if (tmp < _minAns) _minAns = tmp;
        }
        
        Console.WriteLine(_minAns);
    }
}