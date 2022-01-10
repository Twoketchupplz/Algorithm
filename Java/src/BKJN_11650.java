// https://www.acmicpc.net/status?user_id=twoketchupplz&problem_id=11650&from_mine=1

import java.util.Arrays;
import java.util.Scanner;

public class BKJN_11650 {
	static int N;
	static int[][] crdnts;
	static Scanner scin = new Scanner(System.in);
	
	
	public static void main(String[] args) {
		N = scin.nextInt();
		crdnts = new int[N][2];
		
		for (int i = 0; i < N; i++) {
			crdnts[i][0] = scin.nextInt();
			crdnts[i][1] = scin.nextInt();
		}
		Arrays.sort(crdnts, (o1, o2) -> {
			if (o1[0] == o2[0]) {
				return o1[1] - o2[1];
			} else {
				return o1[0] - o2[0];
			}
		});
		
		for (int i = 0; i < N; i++) {
			System.out.println(crdnts[i][0] + " " + crdnts[i][1]);
		}
		
	}
}
