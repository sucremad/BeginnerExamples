package SearchAlg;
import java.util.*;

public class linearTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array= {2,-3,26,999,45,74,23,25,55,21,2,-2,-3,45};
		
		try (Scanner inputi = new Scanner(System.in)) {
			System.out.print("The number that you are looking for: ");
			int number = inputi.nextInt();
			linearSearch.search(array, number);
		}
	}

}
