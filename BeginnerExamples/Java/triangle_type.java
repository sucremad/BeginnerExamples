package first_lab;
import java.util.*;

public class question2 {

	public static void main(String[] args)
	{
		
		Scanner sides=new Scanner(System.in);
		
		System.out.println("First Side:");
		float side1=sides.nextFloat();
		
		System.out.println("Second Side:");
		float side2=sides.nextFloat()
;
		System.out.println("Third Side:");
		float side3=sides.nextFloat();
		
		
		sides.close();
		
		//A triangle or not?
		
		if(side1+side2>side3 && side1+side3>side2 && side2+side3>side1) 
		{
			if(side1==side2&&side2==side3)
				System.out.println("EQUILATERAL Triangle");
			
			else if(side1==side2||side2==side3||side1==side3)
				System.out.println("ISOSCELES Triangle");
			
			else
				System.out.println("SCALENE Triangle");
		}
		
		else
			System.out.println("IT IS NOT A TRIANGLE");
		
			
	}
}
