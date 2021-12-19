// https://www.acmicpc.net/problem/11729
// 문제풀이에 타워를 구현할 필요는 없으나,
// 3개의 타워 인스턴스를 구현하고 직접 쌓는 과정을 구현해봄
// 시간초과
using System;
using System.Collections.Generic;

namespace Hanoi {
	class Tower {
		public int num
		{
			get;
		}
		public Stack<int> diskStack = new Stack<int>();

		public Tower(int num)
		{
			this.num = num;
		}

	}

	class Game{
		static int cnt = 1;
		static void Main(string[] args)
		{
			Tower tower1 = new Tower(1);
			Tower tower2 = new Tower(2);
			Tower tower3 = new Tower(3);

			int N = int.Parse(Console.ReadLine());
			for (int i = N; i > 0; i--) tower1.diskStack.Push(i);
			for (int i = 0; i < N-1; i++)
			{
				cnt = cnt * 2 + 1;
			}
			Console.WriteLine(cnt);
			carry(N, tower1, tower2, tower3);
		}

		
		static void carry(int size, Tower pre, Tower pst, Tower dst)
		{
			if(size == 1)
			{
				move(pre, dst);
			}
			else
			{
				carry(size - 1, pre, dst, pst);
				move(pre, dst);
				carry(size - 1, pst, pre, dst);
			}
		}

		static void move(Tower pre, Tower dst)
		{
			dst.diskStack.Push(pre.diskStack.Pop());
			Console.WriteLine(pre.num + " " + dst.num);
			//foreach (int disk in pre.diskStack) Console.WriteLine(disk);
			//Console.WriteLine("- - - -");
			//foreach (int disk in dst.diskStack) Console.WriteLine(disk);
			//Console.WriteLine("* * * * * * * *");
		}
	}

}

