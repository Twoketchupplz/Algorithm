// https://www.acmicpc.net/problem/10951
// 정상적인 종료 방법이 없다

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BKJN_10951 {
	public static void main(String[] args) throws IOException {
		int A, B;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		while((line = br.readLine()) != null) {
			A = line.charAt(0)-'0';
			B = line.charAt(2)-'0';
			System.out.println(A+B);
		}
		
	}
}
