#include <stdio.h>
int Swap(int number)
{
	int a, b;
	a = number % 10;
	b = number / 10;
	return 10 * a + b;
}


int main()
{
	int number;
	printf("Enter a two-digit number:\n");
	scanf_s("%d", &number);
	printf("First :%d\n", number);
	printf("Then %d\n", Swap(number));
	system("pause");
	return 0;

}
