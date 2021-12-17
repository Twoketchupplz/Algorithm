// https://www.acmicpc.net/problem/2562

using System;
using System.Linq;

class MainApp {
	static void Main(string[] args)
	{
		int[] naturalNum = new int[9];
		int max = 0;
		int idx = -1;

		for (int i = 0; i < 9; i++)
		{
			naturalNum[i] = int.Parse(Console.ReadLine());
		}

		foreach(var num in naturalNum.Select((value, index) => new { value, index })){
			if(num.value > max)
			{
				max = num.value;
				idx = num.index;
			}
		}

		Console.WriteLine(max);
		Console.WriteLine(idx+1);

	}
}