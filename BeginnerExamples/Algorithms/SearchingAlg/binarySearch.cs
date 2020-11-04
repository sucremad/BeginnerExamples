using System;

namespace data_deneme
{
    class Program
    {
        public static int Find_Recursive(int[] numbers, int the_number,int first_index,int last_index)
        {
            int mid_index = (first_index+last_index+1) / 2;

            if (last_index >= first_index)
            {
                if (numbers[mid_index] == the_number)
                {
                    return mid_index;
                }

                 else if (numbers[mid_index] < the_number)
                {

                    return Find_Recursive(numbers, the_number, mid_index + 1, last_index);


                }

                else 
                {

                    return Find_Recursive(numbers, the_number, first_index, mid_index - 1);
                }
                

            }
            else
                return 10000;











        }


        static void Main(string[] args)
        {
            int the_number = 999;
            int[] numbers = { 1, 2, 3, 4, 6, 8, 15, 16, 42, 51, 63, 98, 112, 523, 635, 789, 841, 952, 966, 999 };

            if (Find_Recursive(numbers,the_number,0,19) == 10000)
                Console.WriteLine("Not Found");
            else
                Console.WriteLine("Result:{0}",Find_Recursive(numbers,the_number,0,19));


            Console.ReadKey();
        }
    }
}
