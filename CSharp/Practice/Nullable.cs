using System;

namespace CSharp.Practice
{
    class Nullable
    {
        static void Main(string[] args)
        {
            int? a = null;

            Console.WriteLine(a.HasValue); // False
            Console.WriteLine(a != null); // False

            a = 3;

            Console.WriteLine(a.HasValue); // True
            Console.WriteLine(a != null); // True
            Console.WriteLine(a.Value);
        }
    }
}