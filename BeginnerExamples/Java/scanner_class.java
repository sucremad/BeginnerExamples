package first_lab;
import java.util.*;


public class question1{

	public static void main(String[] args) 
	{
		
		Scanner inputi=new Scanner(System.in);
		
		System.out.println("Who is:");
		String name=inputi.nextLine();
		
		System.out.println("Age:");
		int age=inputi.nextInt();
		
		System.out.println("Female[F] or Male[M] ?");
		char gender=inputi.next().charAt(0);
		
		inputi.close();
		
		System.out.println("Name   :"+name);
		System.out.println("Age    :"+age);
		System.out.println("Gender :"+gender);
		
		
		
		
	}
	
}
