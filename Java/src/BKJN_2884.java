// https://www.acmicpc.net/problem/2884

import java.util.Scanner;

public class BKJN_2884 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 입력 시간을 받으면
		int H = sc.nextInt();
		int M = sc.nextInt();
		// 45분 앞선 시간을 출력
		M -= 45;
		if (M < 0) {
			M += 60;
			H -= 1;
			if (H < 0) {
				H = 23;
			}
		}
		
		System.out.println(H + " " + M);
		
	}
}
