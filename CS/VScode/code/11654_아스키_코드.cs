using System;

class MainApp
{
    static void Main(string[] args)
    {
        char letter = Convert.ToChar(Console.ReadLine());
        int ascii = Convert.ToInt32(letter);

        Console.WriteLine(ascii);
    }
}

