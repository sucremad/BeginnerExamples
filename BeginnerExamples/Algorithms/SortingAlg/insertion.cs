using System;

namespace deneme
{
	class Program
	{
		public static void insertion_sort(int[] array)
		{
			 for (int i =1 ; i < array.Length; i++) {
    	   
    	   for(int j=i-1;j<i&&j>=0;j--) {
    		   
    		   if(array[j]>array[j+1]) {
    			   int temp = array[j];
    			   array[j]=array[j+1];
    			   array[j+1]=temp;
    		   }
    	   }
    	   
		
	}
		}

		static void Main(String[] args)
		{
			int[] array={1,2,-2,66,85,54,36,-3,24,666,-333,568,54,-6,78,24,66};

			insertion_sort(array);

			foreach(int i in array){
				Console.WriteLine(i);
			}

		}
	}
}