using System;

namespace Practice
{
    class FloatConversion
    {
        static void Main(string[] args)
        {
            float a = 69.6875f;
            double b = (double) a;
            Console.WriteLine("a: {0}", a);
            Console.WriteLine("b: {0}", b);
            Console.WriteLine("69.68875 == b: {0}", 69.6875 == b);

            float x = 0.1f;
            double y = (double) x;
            Console.WriteLine("x: {0}", x);
            Console.WriteLine("y: {0}", y);
            Console.WriteLine("0.1 == y: {0}", 0.1 == y);
        }
    }
}