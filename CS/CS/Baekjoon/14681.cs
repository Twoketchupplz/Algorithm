using System;

namespace Baekjoon
{
    public class MainApp
    {
        static void Main(string[] args)
        {
            int x = Int16.Parse(Console.ReadLine());
            int y = Int16.Parse(Console.ReadLine());
            
            if (x > 0 && y > 0)
            {
                Console.WriteLine(1);
            }
            else if (x < 0 && y > 0)
            {
                Console.WriteLine(2);
            }
            else if(x < 0 && y < 0)
            {
                Console.WriteLine(3);
            }
            else
            {
                Console.WriteLine(4);
            }
        }
    }
}