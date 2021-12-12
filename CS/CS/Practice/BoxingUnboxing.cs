using System;

namespace Practice
{
    class BoxingUnboxing
    {
        static void Main(string[] args)
        {
            int a = 123;
            object b = (object) a; // Boxing, store in a heap 
            int c = (int) b; // Unboxing, store in a stack
            
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);

            double x = 3.1414213;
            object y = x; // Boxing
            double z = (double) y; // Unboxing
            
            Console.WriteLine(x);
            Console.WriteLine(y);
            Console.WriteLine(z);
            
        }
    }
}