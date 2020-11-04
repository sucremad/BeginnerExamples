package sum_of_the_numbers;
import java.util.*;

public class sum_of_the_numbers {
	
	//Recursive Function that finds the sum of the numbers up to the given number
	
	static int Recursive_sum(int number) 
	{
		if (number==0)
			return 0;
		else if(number==1)
			return 1;
		else
			return number+Recursive_sum(number-1);
	}
	

	public static void main(String[] args) 
	{
		Scanner input=new Scanner(System.in);
		
		System.out.println("Enter a number");
		int number=input.nextInt(); //takes integer input
		
		System.out.printf("Result:%d",Recursive_sum(number));
		
		
		

	}

}
