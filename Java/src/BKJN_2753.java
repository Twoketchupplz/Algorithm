import java.util.Scanner;

public class BKJN_2753
{
	public static void main (String[] args) {

		Scanner sc = new Scanner(System.in);
		int Year = sc.nextInt();

		if (Year % 400 == 0) {
			System.out.println(1);
		} else if (Year % 4 == 0 && Year % 100 != 0) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}
}
