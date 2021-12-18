// https://www.acmicpc.net/problem/2739

using System;

class Gugudan
{


    static void Main(string[] args)
    {
        string N;
        int dan;
        N = Console.ReadLine();
        dan = int.Parse(N);

        for(int i = 1; i < 10; i++){
            Console.WriteLine("{0} * {1} = {2}", dan, i, dan*i);
        }
    }

}