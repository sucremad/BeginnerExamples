package first_lab;
import java.util.*;

public class question3 {
	
	
	public static int Facto(int number) 
	{
		if(number==0||number==1)
			return 1;
		else
			return number*Facto(number-1);
	}

	public static void main(String[] args) 
	{
		Scanner take=new Scanner(System.in);
		
		System.out.println("Enter a number:");
		
		int number =take.nextInt();
		
		take.close();
		
		System.out.println("Result:"+Facto(number));
		
		
	}
	
}
	
