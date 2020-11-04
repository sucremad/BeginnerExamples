package first_lab;
import java.util.*;

public class fibonacci {
	
	
	public static  int Fibonacci_Recursive(int number) 
	{
		if(number==0) 
		{
			return 0;
		}
		else if(number==1)
			return 1;
		
		else 
		{
			return Fibonacci_Recursive(number-1) + Fibonacci_Recursive(number-2);
		}
	}
	
	public static void main(String[] args) 
	{
		Scanner taken= new Scanner(System.in);
		
		System.out.println("Enter a number:");
		
		int the_number=taken.nextInt();
		
		taken.close();
		System.out.printf("Result:%d",Fibonacci_Recursive(the_number));
		
		 
		 
		 
	}
	

}
