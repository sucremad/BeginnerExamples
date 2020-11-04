package SearchAlg;
public class linearSearch {
	
	public static void search(int[] array,int number) 
	{
		boolean  var=false;
		
		for (int i=0;i<array.length;i++) 
		{
			if(array[i]==number) {
				System.out.println("Number found in  "+i+". index");
				var=true;
			}
		

				
		}
		
		if (!var) {
			System.out.println("Does not exit!");
		}
	}

}
