// https://www.acmicpc.net/problem/10818

using System;

class MainApp {
    static void Main(string[] args) {
        int N, k;
        int min = 1000000;
        int max = -1000000;
        string[] str;

        N = int.Parse(Console.ReadLine());
        str = Console.ReadLine().Split(' ');

        for (int i = 0; i < N; i++) {
            k = int.Parse(str[i]);
            if (min > k) min = k;
            if (max < k) max = k;
        }

        Console.WriteLine("{0} {1}", min, max);

    }
}